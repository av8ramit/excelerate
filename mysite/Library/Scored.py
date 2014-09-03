####################################################################################################################################################  
#                                                                                                                                                  #
# This file has been generated by Amit Patankar:                                                                                                   #
#     Created by              : amit.patankar                                                                                                      #    
#     Created on              : 11-07-2013                                                                                                         #
#     Directory               : /Desktop/                                                                                                          #
#     Purpose                 : This structure holds the attributes of each section in a text.                                                     #
#                                                                                                                                                  #
#################################################################################################################################################### 

import csv
from Values import *
from Key import *
from Data import *

class Scored_Test(object):

    #This is the default constructor with all variables defined.
    def __init__(self, test_id):
        self.test_id = test_id
        self.sections = {}
        self.missed_questions_index = {}
        self.missed_questions = {}
        self.missed_questions[WRITING_TYPE] = []
        self.missed_questions[MATH_TYPE] = []
        self.missed_questions[READING_TYPE] = []
        self.test_summary = None
        self.score_summary = None
        self.data = Data_Holder()
        self.qtypedict = {}
        self.essay = 7
        self.date = ''

    #This sets the test summary upon creation and recreation.
    def set_summary(self, s):
        self.test_summary = s

    #This returns the section.
    def get_section(self, section_number):
        return self.sections[index]

    #This adds the scored section to the text.
    def add_section(self, section):
        assert(type(section) == Scored_Section)
        self.sections[section.index] = section

    #This returns the scored test id.
    def get_id(self):
        return self.test_id

    def make_sections(self, missed_array, section_type):
        current_section = Scored_Section(0, 0, 0, 0)
        for entry in missed_array:
            section_index = int(entry[0].split('_')[-2])         
            index = int(entry[0].split('_')[-1])
            q_id = entry[0]
            attempt = entry[1]
            if index != current_section.index:
                if current_section.is_valid():
                    current_section.qa = current_section.size - current_section.qb - current_section.qm
                    current_section.score = current_section.qa - round_rem(float(current_section.qm)/4)
                    self.add_section(current_section)
                current_section = self.sections[section_index]          

            #fill section summary
            if attempt == "?":
                self.missed_questions_index[section_index][index] = attempt
                self.test_summary.reports[section_type].add_blank()
                current_section.add_blank()             
            else:
                self.missed_questions_index[section_index][index] = attempt         
                self.test_summary.reports[section_type].add_miss()
                current_section.add_miss()              
            self.test_summary.reports[section_type].incorrect_questions.append(entry)

            q = Scored_Question(current_section, q_id, attempt)
            self.qtypedict[q_id[6:]]= q.question_type
            current_section.add_question(q)
            self.missed_questions[section_type].append(entry)
            self.test_summary.reports[section_type].incorrect_questions.append(entry)

        #add last section
        if current_section.is_valid():
            current_section.qa = current_section.size - current_section.qb - current_section.qm
            current_section.score = current_section.qa - round_rem(float(current_section.qm)/4)
            self.add_section(current_section)

        self.test_summary.reports[section_type].qa = section_size(section_type) - self.test_summary.reports[section_type].qm - self.test_summary.reports[section_type].qb
        self.score_summary = Score_Summary(self.test_summary)

    #This recreates a scored test when given section information for missed question tuples.
    def recreate(self, sections):
        #sections will be passed in a dictionary indexed by type
        key = {}
        #key[index] = (section_type, size)
        #read from keyfile and create section shells for scored test based on type and index
        with open(test_directory(self.test_id) + DIR_SEP + KEYFILE, 'rU') as f:
            reader = csv.reader(f)
            for row in reader:
                if row != KEY_VECTOR or row[0] == '':
                    index = int(row[0])
                    section_type = int(row[1])
                    size = int(row[2])
                    if section_type == TRIAL_TYPE:
                        continue                    
                    key[index] = (section_type, size)
                    if section_type == WRITING_TYPE:
                        self.missed_questions_index[index] = {}
                        self.sections[index] = Scored_Section(self, index, section_type, size)
                    elif section_type == MATH_TYPE:
                        self.missed_questions_index[index] = {}
                        self.sections[index] = Scored_Section(self, index, section_type, size)
                    elif section_type == READING_TYPE:
                        self.missed_questions_index[index] = {}
                        self.sections[index] = Scored_Section(self, index, section_type, size)

        #from sections missed questions, recreate into this scored test
        #current_section = Scored_Section(0, 0, 0, 0)

        #create Test Summary for Scored Test
        self.test_summary = Test_Summary(self.test_id)
        self.test_summary.essay = self.essay

        #WRITING RECONSTRUCTION
        self.make_sections(sections[WRITING_TYPE], WRITING_TYPE)

        #MATH RECONSTRUCTION
        self.make_sections(sections[MATH_TYPE], MATH_TYPE)

        #READING RECONSTRUCTION
        self.make_sections(sections[READING_TYPE], READING_TYPE)


    #String override method.
    def __str__(self):
        output = endl + "TEST_ID: " + self.test_id + endl
        output += endl
        output += ("DATE: " + self.date + endl)
        output += ("ESSAY: " + str(self.essay) + endl)              
        output += "WRITING:" + endl
        output += "Missed Questions:"
        output += str(self.missed_questions[WRITING_TYPE])
        output += endl
        output += endl
        output += "MATH:" + endl
        output += "Missed Questions:"
        output += str(self.missed_questions[MATH_TYPE])
        output += endl
        output += endl
        output += "READING:" + endl
        output += "Missed Questions:"
        output += str(self.missed_questions[READING_TYPE])
        output += endl
        output += endl
        output += SECTION_SEP
        output += endl
        return output

class Scored_Section(object):

    #This is the default constructor with all variables defined.
    def __init__(self, scored_test, index, section_type, size):
        self.scored_test = scored_test
        self.index = index
        self.type = section_type
        #self.section_summary = None
        self.missed_questions = []
        self.size = size
        self.score = 0      
        self.qa = 0
        self.qm = 0
        self.qb = 0

    #This sets the score for the section
    def set_score(self, score):
        self.score = score

    #This adds a missed question.
    def add_miss(self):
        self.qm += 1

    #This adds a blank question.
    def add_blank(self):
        self.qb += 1

    def calc_qa(self):
        self.qa = self.size - self.qm - self.qb

    def calc_score(self):
        self.score = self.qa - self.qm/4 - round_rem(float(self.qm)/4)      

    #This adds the section summary for the section.
    def add_summary(self, qa, qm, qb):
        self.question_summary = Section_Summary(qa, qm, qb)

    #This adds a question.
    def add_question(self, q):
        self.missed_questions.append(q)

    #This returns the scored section id.
    def get_id(self):
        return self.scored_test.get_id() + FIELD_SEP + str(self.index)

    #This returns if the section is valid. Used in section recreation.
    def is_valid(self):
        return self.index != 0

    #String override method.
    def __str__(self):
        output = self.get_id()
        output += endl
        output += (section_name(self.type) + endl)
        output += ("QA: " + str(self.qa) + endl)
        output += ("QM: " + str(self.qm) + endl)
        output += ("QB: " + str(self.qb) + endl)
        output += ("Raw Score: " + str(self.score) + endl)
        return output

#Base Scored Question Class
class Scored_Question(object):

    #This is the default constructor with all variables defined.
    def __init__(self, scored_section, q_id, incorrect_answer):
        self.scored_section = scored_section
        self.index = None
        self.correct_answer = None
        self.incorrect_answer = incorrect_answer
        self.difficulty = None
        self.question_type = None
        self.make_by_id(q_id)

    #This is the default constructor with all variables defined.
    def make_by_id(self, q_id):
        array = q_id.split('_')
        #test_id = array[0] + '_' + array[1]
        test_id = fuse_id_array(array[:-2])
        filename = test_id + DIR_SEP + "Section " + array[-2] + ".csv"
        number = array[-1]
        with open(test_directory(filename), 'rU') as f:
            reader = csv.reader(f)
            for row in reader:
                if row[NUMBER_INDEX] == number:
                    break

        self.index = int(row[NUMBER_INDEX])
        self.correct_answer = row[ANSWER_INDEX]
        self.difficulty = int(row[DIFFICULTY_INDEX])
        self.question_type = row[TYPE_INDEX]


    #This returns the scored question id.
    def get_id(self):
        return self.scored_section.get_id() + FIELD_SEP + str(num)

#class to make question objects for class analytics, questions missed by majority of class
class Class_Question(object):
    def __init__(self, q, freq):
            self.question = q
            self.frequency = freq



