import csv
import os

filename = 'crap.csv'

#Converts a test from Elite standard to Excelerate databse

def convert_row(row, FORM_CODE):
    target_math = None
    SECTION_INDEX = 9
    TYPE_INDEX = 10
    ANSWER_INDEX = 11
    LEVEL_INDEX = 12
    answers = row[ANSWER_INDEX]
    array = []
    if row[TYPE_INDEX] == '1':
        section_type = 'M'
    if row[TYPE_INDEX] == '2':
        section_type = 'R'
    if row[TYPE_INDEX] == '3':
        section_type = 'W'
    array.append("Number,Answer,Difficulty,Range,Type\n")
    f = open(FORM_CODE + '/' + 'Section ' + row[SECTION_INDEX] + '.csv', 'w')

    assert(len(row[ANSWER_INDEX]) == len(row[LEVEL_INDEX]))
    if len(row[ANSWER_INDEX]) in [10,8,6]:
        target_math = row[SECTION_INDEX]
    for i in range(0, len(row[ANSWER_INDEX])):
        array.append(str(i+1) + ',' + answers[i] + ',' + row[LEVEL_INDEX][i] + ',' + 'N' + ',' + section_type + '\n')

    f.writelines(array)
    f.close()
    return target_math

def add_fillin(FORM_CODE, array1, target_math):
    filename = FORM_CODE + '/' + 'Section ' + target_math + '.csv'
    array = []
    with open(filename, 'rU') as f:
        reader = csv.reader(f)
        for row in reader:
            array.append(str(row)[1:-1] + '\n')
    array += array1
    print (array1)
    filename = open(filename, 'w')
    filename.writelines(array)
    filename.close()

def convert_range(answer):
    if ';' in answer:
        a = answer.split(';')
        return ('(' + a[0] + ',' + a[1] + ')')
    elif '<' in answer:
        a = answer.split('<')
        return ('(' + a[0] + ',' + a[2] + ')')

with open(filename, 'rU') as f:

    target_math = None
    reader = csv.reader(f)
    for row in reader:
        FORM_CODE = row[0]
        os.mkdir(FORM_CODE)
        a = convert_row(row, FORM_CODE)
        if a != None:
            target_math = a
        break

    array =[]
    for row in reader:
        print(row)
        if row[9] != '':
            FORM_CODE = row[0]
            a = convert_row(row, FORM_CODE)
            if a != None:
                target_math = a
        else:
            array.append(row[14] + ',' + row[15] + ',' + row[16] + ',' + 'Y' + ',' + 'M' + '\n')

    add_fillin(FORM_CODE, array, target_math)
            




