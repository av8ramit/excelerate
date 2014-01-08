####################################################################################################################################################  
#  																																				   #
# This file has been generated by Amit Patankar:  																								   #
#     Created by              : amit.patankar																									   #	
#     Created on              : 08-08-2013																										   #
#     Directory               : /Desktop/																								           #
#     Purpose		    	  : This file holds all the command functions.												   						   #
#  													   																							   #
#################################################################################################################################################### 

import csv

from Values import *
from Key import *
from Answer import *
from User import *

def clear(n):
	for i in range(0,n):
		print n

def new_user(name):
	directory = "Users" + DIR_SEP + name
	if (file_exists(directory)):
		rmdir(directory)
	u = User(name)
	u.build()
	return u

def load_user(name, filename):
	u = User(name)
	u.name = name
	u.recreate_user(filename)
	return u

def grade(u, filename):
	pa = parse_answers(filename)
	u.grade(pa)

def make_answer_sheet(u, test_id):
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

	FILE = open(u.directory() + DIR_SEP + test_id + ".csv", "w")
	FILE.writelines(lines)
	FILE.close()

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
    		elif row == []:
	    		continue
	    	elif row[0] == "": #blanks
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

def simple_report(u):
	u.simple_report()


#def valid_test(filename):
	
