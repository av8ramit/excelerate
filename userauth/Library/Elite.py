####################################################################################################################################################  
#                                                                                                                                                  #
# This file has been generated by Amit Patankar:                                                                                                   #
#     Created by              : amit.patankar                                                                                                      #    
#     Created on              : 17-04-2014                                                                                                         #
#     Directory               : /Progs/Excelerate/Library                                                                                          #
#     Purpose                 : This structure converts the Excel file into our text file                                                              #
#                                                                                                                                                  #
####################################################################################################################################################

from Values import *
from Scored import *
from Commands import *
from User import *
import os
import csv
import shutil

#Base Elite Class Class

TEST_ID_INDEX = 0
STUDENT_ID_INDEX = 1
TEST_DATE_INDEX = 2
FORM_CODE = 3
MATH_INDEX = 5
READING_INDEX = 6
ESSAY_INDEX = 7
WRITING_INDEX = 8
SECTION_1 = 9
SECTION_2 = 10
SECTION_3 = 11
SECTION_4 = 12
SECTION_5 = 13
SECTION_6 = 14
SECTION_7 = 15
SECTION_8 = 16
SECTION_9 = 17
SECTION_10 = 18
DIFFERENCE = 8
GRID_1 = 19
GRID_2 = 20
GRID_3 = 21
GRID_4 = 22
GRID_5 = 23
GRID_6 = 24
GRID_7 = 25
GRID_8 = 26
GRID_9 = 27
GRID_10 = 28
MATH_SCALED = 38
READING_SCALED = 39
WRITING_SCALED = 40
GRIGHT1 = 59
GRIGHT2 = 60
GRIGHT3 = 61
GRIGHT4 = 62
GRIGHT5 = 63
GRIGHT6 = 64
GRIGHT7 = 65
GRIGHT8 = 66
GRIGHT9 = 67
GRIGHT10 = 68

run = 2

if run == 1:
    DEBUG = True
    REPORTS = False
    SANITY = False
elif run == 2:
    DEBUG = True
    REPORTS = True
    SANITY = True

class Elite_Class(object):

    def __init__(self, filename):
        self.students = {}
        self.valid_tests = list_tests()
        self.averages = {}
        self.elite_scores = {} #debug dictionary
        self.invalid_rows = []
        self.corrupted_rows = {}
        self.total_tests = 0

        self.convert_database(filename)


    #main script function that creates Elite class
    def convert_database(self, filename):
        with open(filename, 'rU') as f:
            reader = csv.reader(f)
            #waive various line entries you know are bogus
            waive_array = [246, 726, 438, 564, 555, 1125, 404, 744, 980, 231, 1045, 823, 265]
            #[555, 1045, 823, 726, 231, 404, 744, 980, 265, 438, 564, 246]
            # 231, 26, 228, 555, 246, 438, 564, 265, 404, 744, 786, 726
            for row in reader:
                SID = row[STUDENT_ID_INDEX]
                if SID not in self.corrupted_rows.keys():
                    self.corrupted_rows[SID] = []
                if not self.valid_row(row):
                    self.invalid_rows.append(row)
                    continue
                self.total_tests += 1
                if SID not in self.students.keys():
                    self.students[SID] = User(SID, 'Elite')
                if SID not in self.elite_scores.keys():
                    self.elite_scores[SID] = []

                userid = row[STUDENT_ID_INDEX]
                test_id = row[FORM_CODE]
                test_date = date_converter(row[TEST_DATE_INDEX])

                #hashing the test date in average key
                if test_date not in self.averages.keys():
                    self.averages[test_date] = {}
                    self.averages[test_date][MATH_TYPE] = []
                    self.averages[test_date][READING_TYPE] = []
                    self.averages[test_date][WRITING_TYPE] = []

                self.averages[test_date][WRITING_TYPE].append(int(row[WRITING_SCALED]))
                self.averages[test_date][MATH_TYPE].append(int(row[MATH_SCALED]))
                self.averages[test_date][READING_TYPE].append(int(row[READING_SCALED]))

                if int(row[0]) in waive_array:
                    self.corrupted_rows[SID].append(Corrupted_Entry(row))
                    continue

                user_test = Scored_Test(test_id)
                user_test.date = row[TEST_DATE_INDEX]
                if (is_int(row[ESSAY_INDEX]) and int(row[ESSAY_INDEX]) > 0):
                    user_test.essay = row[ESSAY_INDEX]
                else:
                    user_test.essay = 1
                test_key = self.key_test(test_id)
                for index in range(SECTION_1, SECTION_10 + 1):
                    array = self.convert_section(index, row[index], test_id, row)
                    section_type = test_key[index - DIFFERENCE]
                    if section_type == READING_TYPE or section_type == WRITING_TYPE or section_type == MATH_TYPE:
                        user_test.missed_questions[test_key[index - DIFFERENCE]] += array
                self.students[SID].tests_taken.append(user_test)
                self.elite_scores[SID].append(self.enter_entry(row))

        #map-reduce on average data
        for test in self.averages.keys():
            self.averages[test][WRITING_TYPE] = average_array(self.averages[test][WRITING_TYPE])
            self.averages[test][READING_TYPE] = average_array(self.averages[test][READING_TYPE])
            self.averages[test][MATH_TYPE] = average_array(self.averages[test][MATH_TYPE])


        #Create average file in class folder
        new_class('Elite')
        filename = class_directory('Elite') + DIR_SEP + "average.txt"
        array = []
        with open(filename, 'w') as f:
            for key in self.averages:
                array.append("TEST_DATE: " + key + endl)
                array.append("WRITING: " + str(self.averages[key][WRITING_TYPE]) + endl)
                array.append("READING: " + str(self.averages[key][READING_TYPE]) + endl)
                array.append("MATH: " + str(self.averages[key][MATH_TYPE]) + endl)
                array.append(SECTION_SEP + endl)
                array.append(endl)
            f.writelines(array)
            f.close()


        #Debug mode flag and Report print flags

        error = 1
        error_array = []
        tests_entered = 0

        #Create students based on parsed analysis
        for student in self.students.keys():
            new_user(student, 'Elite')
            self.students[student].save_user()
            u = load_user(student, user_filename(student,'Elite'), 'Elite')

            #Debug mode report printing
            if DEBUG:
                test_index = 0
                for test in u.tests_taken:
                    tests_entered += 1
                    e = self.elite_scores[student][test_index]
                    assert (e.row[TEST_DATE_INDEX] == test.date) #verifies date and form code
                    assert (e.row[FORM_CODE] == test.test_id)
                    mistake = False


                    #Score injection if raw scores match
                    if e.writing_raw_score == test.score_summary.writing_score:
                        test.score_summary.section_scores[WRITING_TYPE] = e.writing_scaled_score

                    if e.reading_raw_score == test.score_summary.reading_score:
                        test.score_summary.section_scores[READING_TYPE] = e.reading_scaled_score

                    if e.math_raw_score == test.score_summary.math_score:
                        test.score_summary.section_scores[MATH_TYPE] = e.math_scaled_score

                    if e.writing_scaled_score != test.score_summary.section_scores[WRITING_TYPE]:
                        print("Writing score was incorrect for test " + student + " for test " + test.test_id)
                        print("Elite: " + str(e.writing_scaled_score) + " Excelerate: " + str(test.score_summary.section_scores[WRITING_TYPE]))
                        print("Elite: " + str(e.writing_raw_score) + " Excelerate: " + str(test.score_summary.writing_score))
                        print ("Essay: " + str(test.essay))
                        mistake = True

                    if e.reading_scaled_score != test.score_summary.section_scores[READING_TYPE]:
                        print("Reading score was incorrect for test " + student + " for test " + test.test_id)
                        print("Elite: " + str(e.reading_scaled_score) + " Excelerate: " + str(test.score_summary.section_scores[READING_TYPE]))
                        print("Elite: " + str(e.reading_raw_score) + " Excelerate: " + str(test.score_summary.reading_score))
                        mistake = True

                    if e.math_scaled_score != test.score_summary.section_scores[MATH_TYPE]:
                        print("Math score was incorrect for test " + student + " for test " + test.test_id)
                        print("Elite: " + str(e.math_scaled_score) + " Excelerate: " + str(test.score_summary.section_scores[MATH_TYPE]))
                        print("Elite: " + str(e.math_raw_score) + " Excelerate: " + str(test.score_summary.math_score))
                        mistake = True

                    if mistake:
                        print ("Row Number: " + str(e.number))
                        error_array.append(int(e.number))
                        print ("Error Index: " + str(error))
                        error += 1
                        print (endl)
                    test_index += 1


            #Enter Corrupted Test Scores
            if student in self.corrupted_rows.keys():
                for entry in self.corrupted_rows[student]:
                    tests_entered += 1
                    variable = 0
                    for t in u.tests_taken:
                        if date_after(entry.row[TEST_DATE_INDEX], t.date):
                            break
                        variable +=1
                    u.tests_taken.insert(variable, entry.return_test()) #in case last test is shadow test

            #Working on Sanity testbench
            if SANITY:
                for elite_test in self.elite_scores[student]:
                    exists = False
                    for test in u.tests_taken:
                        writing_exists = False
                        reading_exists = False
                        math_exists = False
                        if elite_test.writing_scaled_score == test.score_summary.section_scores[WRITING_TYPE]:
                            writing_exists = True
                        if elite_test.reading_scaled_score == test.score_summary.section_scores[READING_TYPE]:
                            reading_exists = True
                        if elite_test.math_scaled_score == test.score_summary.section_scores[MATH_TYPE]:
                            math_exists = True
                        exists = (writing_exists and reading_exists and math_exists) or exists #exists if this matches or has matched before
                    assert (exists)

            #print Reports
            if (REPORTS):
                simple_report(u)
                advanced_report(u)
                section_report(u)
                graph_report(u)
                shutil.copy2('reports.html', 'Users/Elite/' + student)

        if len(error_array) != 0:
            print(error_array)
            print("Total Errors: " + str(len(error_array)))
        else:
            print("NO ERRORS WERE REPORTED!!!")

        if SANITY:
            print ("Tests Expected:" + str(self.total_tests))
            print("Tests Seen: " + str(tests_entered))
            print("Students Analyzed: " + str(len(self.students.keys())))
            print("SANITY TEST PASSED!!!")

        #if run == 1:
        #    print("Invalid Rows: " + str(self.invalid_rows))

        #Run report analysis with arrays that were not included
        array = []
        with open('runreport.txt', 'w') as f:
            array.append(str(len(self.invalid_rows)) + endl)
            for row in self.invalid_rows:
                array.append(str(row) + endl)
            f.writelines(array)
            f.close()

    #returns if row is valid entries
    def valid_row(self, row):
        if 'Test_ID' and 'Student_ID' in row: #first row
            return False
        if row[FORM_CODE] not in self.valid_tests:
            return False
        if row[MATH_INDEX] == '-100' or row[MATH_INDEX] == '0':
            return False
        a = [MATH_INDEX, WRITING_INDEX, READING_INDEX]
        for index in a:
            if int(row[index]) <= 0:
                return False
        return True

    #convert a section into answers and a score
    def convert_section(self, section_index, results_string, test_id, row):
        section_number = section_index - DIFFERENCE
        question_index = 0
        missed_array = []
        for char in results_string:
            question_index += 1
            q_id = test_id + FIELD_SEP + str(section_number) + FIELD_SEP + str(question_index)
            if char != '+':
                if char == 'O': #left blank
                    entry = (q_id, '?')
                else: #incorrect
                    entry = (q_id, char)
                missed_array.append(entry)
        if self.math_grid(test_id, section_number):
            for index in range(GRIGHT1, GRIGHT10 + 1):
                result = row[index]
                #print (result)
                if result != '+':
                    q_id = test_id + FIELD_SEP + str(section_number) + FIELD_SEP + str(len(results_string)+(index-18))
                    entry = (q_id, '?')
                    missed_array.append(entry)                    
        return missed_array

    #returns if a section is a math grid
    def math_grid(self, test_id, section_id):
        filename = test_directory(test_id) + "/Section " + str(section_id) + CSV 
        if not file_exists(filename):
            return False
        with open(filename, 'rU') as f:
            reader = csv.reader(f)
            for row in reader:
                if row[RANGE_INDEX] == "Y":
                    return True
        return False

    #translate grid answer and is disabled
    def translate_grid_answer(self, answer, key_answer):
        attempt = None
        if answer == '':
            return 'BLANK','?'
        try:
            if '/' in answer:
                num = answer.split('/')[0]
                sub = answer.split('/')[1]
                attempt = round(div(num, sub),3)
            elif '.' in answer:
                attempt = float(answer)
            else:
                attempt = int(answer)
        except:
            attempt = "A"

        answer = key_answer
        if '(' in answer and ')' in answer:
            answer = answer.replace(' ','')
            answer = answer.replace('(','')
            answer = answer.replace(')','')
            lower_limit = float(answer.split(',')[0])
            upper_limit = float(answer.split(',')[1])
            if attempt >= lower_limit and attempt <= upper_limit:
                return "CORRECT"
        elif attempt == float(answer):
            return "CORRECT"
        return "INCORRECT",str(attempt)

    #return dictionary of section index to type
    def key_test(self, test_id):
        test_dict = {}
        with open(test_directory(test_id) + DIR_SEP + KEYFILE, 'rU') as f:
            reader = csv.reader(f)
            for row in reader:
                if row != KEY_VECTOR:
                    test_dict[int(row[KEY_INDEX])] = int(row[KEY_TYPE])
        return test_dict

    #take a row and make an Excelerate entry
    def enter_entry(self, row):
        entry = Elite_Test_Entry(row[FORM_CODE], row)
        entry.number = row[0]
        entry.writing_raw_score = int(row[WRITING_INDEX])
        entry.reading_raw_score = int(row[READING_INDEX])
        entry.math_raw_score = int(row[MATH_INDEX])
        entry.writing_scaled_score = int(row[WRITING_SCALED])
        entry.reading_scaled_score = int(row[READING_SCALED])
        entry.math_scaled_score = int(row[MATH_SCALED])
        return entry

                
class Elite_Test_Entry(object):

    #initialize Elite Test Entry
    def __init__(self, test_id, row):
        self.id = test_id
        self.number = 0
        self.row = row
        self.writing_raw_score = 0
        self.reading_raw_score = 0
        self.math_raw_score = 0
        self.writing_scaled_score = 0
        self.reading_scaled_score = 0
        self.math_scaled_score = 0

class Corrupted_Entry(object):

    def __init__(self, row):
        self.writing_scaled_score = int(row[WRITING_SCALED])
        self.reading_scaled_score = int(row[READING_SCALED])
        self.math_scaled_score = int(row[MATH_SCALED])
        self.row = row

    def return_test(self):
        st = Scored_Test(self.row[FORM_CODE])
        st.score_summary = Corrupted_Score_Summary(self)
        if is_int(self.row[ESSAY_INDEX]):
            st.essay = int(self.row[ESSAY_INDEX])
        else:
            st.essay = 7
        st.date = self.row[TEST_DATE_INDEX]
        return st

class Corrupted_Score_Summary(object):

    #Creates a Score summmary indexed by section based upon a test summary.
    def __init__(self, CE):
        self.id = CE.row[FORM_CODE]
        self.section_scores = {}        
        self.section_scores[WRITING_TYPE] = CE.writing_scaled_score
        self.section_scores[READING_TYPE] = CE.reading_scaled_score
        self.section_scores[MATH_TYPE] = CE.math_scaled_score

    def total_score(self):
        score = 0
        for s in self.section_scores.values():
            score += s
        return score

a = Elite_Class('Elite/Elite828.csv')