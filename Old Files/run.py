import sys
import csv
sys.path.append('Statardized')

from Values import *
from Test import *
from Section import *
from Answer import *

def make_answer_sheet(test_id):
	filename = test_id
	lines = []

	label_vector = "Number:,Answer:\n"
	lines.append(test_id + " Answer Sheet\n\n")
	lines.append(label_vector)

	with open(filename + DIR_SEP + KEYFILE, 'rU') as f:
	    reader = csv.reader(f)
	    for row in reader:
			if row != KEY_VECTOR:

				lines.append("Section " + str(row[0]) + ":" + endl)
				for j in range(1,int(row[2]) + 1):
					lines.append(str(j) + ",?")
					lines.append(endl)

	FILE = open(test_id + ".csv", "w")
	FILE.writelines(lines)
	FILE.close()

make_answer_sheet("10_09")

def import_test(test_id):
	t = test_id.split("_")
	test = Test(t[0], t[1])

	key = {}
	with open(test_id + DIR_SEP + KEYFILE, 'rU') as f:
	    reader = csv.reader(f)
	    for row in reader:
	    	if row != KEY_VECTOR:
	    		key[row[0]] = (row[KEY_TYPE],row[KEY_SIZE])
	for number in key.keys():
		if number == '1': #essay
			es = Essay_Section(test)
			test.add_section(es)
		elif key[number][1] == '0': #trial
			ts = Trial_Section(test, int(number))
			test.add_section(ts)
		else: #real
			s = Section(test, int(number), int(key[number][0]))
			s.parse_questions(test_id + DIR_SEP + "Section " + number + ".csv")
			test.add_section(s)
	return test
#import_test("10_09")

def parse_answers(filename):
	with open(filename, 'rU') as f:
	    reader = csv.reader(f)
	    id_set = False
	    counter = 1
	    test = None
	    current_section = None

	    for row in reader:
	    	counter +=1
	    	if row == ANSWER_VECTOR:
	    		continue
	    	elif not id_set:
	    		test_id = row[0].split(' ')[0]
	    		id_set = True
	    		test = Answered_Test(test_id)

	    	elif len(row) > 0 and row[0].split(' ')[0] == "Section":
	    		index = row[0].split(' ')[1][:-1]
	    		if current_section != None:
	    			test.add_section(current_section)

	    		current_section = Answered_Section(int(index))

	    	elif len(row) != 0:
	    		q_num = int(row[0])
	    		answer = row[1]
	    		q = Answered_Question(q_num, answer)
	    		current_section.add_question(q)
	test.add_section(current_section)
	return test

def main():
	make_answer_sheet("10_09")
	a = parse_answers("10_09.csv")
	t = import_test("10_09")
	print(t.grade(a))

main()




	
