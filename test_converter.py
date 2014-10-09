import csv
import os

ESSAY_SECTION_INDEX = 1
LABEL_VECTOR = ['Number', 'Answer', 'Difficulty', 'Range', 'Type']
READING_TYPE = 0
WRITING_TYPE = 1
MATH_TYPE = 2
ESSAY_TYPE = 3  

ELITE_MATH_TYPE = '1'
ELITE_READING_TYPE = '2'
ELITE_WRITING_TYPE = '3'

TYPE_CONVERTER = {}
TYPE_CONVERTER[ELITE_MATH_TYPE] = MATH_TYPE
TYPE_CONVERTER[ELITE_READING_TYPE] = READING_TYPE
TYPE_CONVERTER[ELITE_WRITING_TYPE] = WRITING_TYPE 

QUESTION_CONVERTER = {}
QUESTION_CONVERTER['2S'] = 'R1'
QUESTION_CONVERTER['2M'] = 'R2'
QUESTION_CONVERTER['2D'] = 'R3'
QUESTION_CONVERTER['2P'] = 'R4'
QUESTION_CONVERTER['2I'] = 'R5'
QUESTION_CONVERTER['2C'] = 'R6'
QUESTION_CONVERTER['2T'] = 'R7'
QUESTION_CONVERTER['2V'] = 'R8'

QUESTION_CONVERTER['3S'] = 'W1'
QUESTION_CONVERTER['3E'] = 'W2'
QUESTION_CONVERTER['3P'] = 'W3'

QUESTION_CONVERTER['1M'] = 'M1'
QUESTION_CONVERTER['1A'] = 'M2'
QUESTION_CONVERTER['1G'] = 'M3'
QUESTION_CONVERTER['1D'] = 'M4'




filename = 'answer_key.csv'
testcode = 'RC02'
FORM_CODE = 0
SECTION_INDEX = 1
SECTION_TYPE_INDEX = 2
ANSWER_INDEX = 3
DIFFICULTY_INDEX = 4
TYPE_INDEX = 5




key = {} #key = Section Number 

def convert():
    with open(filename, 'rU') as f:
        reader = csv.reader(f)
        for row in reader:
            if row[FORM_CODE] == testcode:
                key[row[SECTION_INDEX]] = (TYPE_CONVERTER[row[SECTION_TYPE_INDEX]], str(len(row[ANSWER_INDEX])))
        os.mkdir('Tests/' + testcode)
        keylines = []
        for i in range(1,11):
            if i == 1:
                keylines.append('Section:,Type:,Size:' + '\n')
                keylines.append('1,3,0' + '\n')
            elif str(i) not in key.keys():
                keylines.append(str(i) + ',4,0' + '\n')
            else:
                keylines.append(str(i) + ',' + str(key[str(i)][0]) + ',' + key[str(i)][1] + '\n')
        keyfile = open('Tests/' + testcode + '/key.csv', 'w')
        keyfile.writelines(keylines)
        keyfile.close()


    with open(filename, 'rU') as f:
        reader = csv.reader(f)
        for row in reader:
            if row[FORM_CODE] == testcode:
                assert row[SECTION_INDEX] in key.keys()
                f = open('Tests/' + testcode + '/Section ' + row[SECTION_INDEX] + '.csv', 'w')              
                flines = []
                flines.append('Number,Answer,Difficulty,Range,Type\n')
                difficulty = row[DIFFICULTY_INDEX]
                types = row[TYPE_INDEX]
                answers = row[ANSWER_INDEX]
                for i in range (0, len(answers)):
                    if difficulty == '':
                        diff = '3'
                    else:
                        diff = difficulty[i]
                    flines.append(str(i+1) + ',' + answers[i] + ',' + diff + ',' + 'N,' + QUESTION_CONVERTER[row[SECTION_TYPE_INDEX] + types[i]] + '\n')
                f.writelines(flines)
                f.close()

convert()

