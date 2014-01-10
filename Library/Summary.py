####################################################################################################################################################  
#                                                                                                                                                  #
# This file has been generated by Amit Patankar:                                                                                                   #
#     Created by              : amit.patankar                                                                                                      #    
#     Created on              : 11-07-2013                                                                                                         #
#     Directory               : /Desktop/                                                                                                          #
#     Purpose                 : This structure is a question summary self.                                                                         #
#                                                                                                                                                  #
#################################################################################################################################################### 

from Values import *
import csv

class Score_Summary(object):

    #Creates a Score summmary indexed by section based upon a test summary.
    def __init__(self, test_summary):
        assert(type(test_summary) == Test_Summary)
        self.id = test_summary.id
        self.section_scores = {}        
        writing_score = test_summary.reports[WRITING_TYPE].raw_score()
        reading_score = test_summary.reports[READING_TYPE].raw_score()
        math_score = test_summary.reports[MATH_TYPE].raw_score()
        self.lookup_score(writing_score, reading_score, math_score)

    #Calculates total score.
    def total_score(self):
        score = 0
        for s in self.section_scores.values():
            score += s
        return score

    #Looks up score in table based upon test scoring sheet.
    def lookup_score(self, ws, rs, ms):
        scores = {}
        scores[MATH_TYPE] = 200
        scores[WRITING_TYPE] = 200
        scores[READING_TYPE] = 200
        with open(self.id + DIR_SEP + SCOREFILE, 'rU') as f:
            reader = csv.reader(f)
            for row in reader:
                if row != SCORE_VECTOR and not empty(row):
                    score = int(row[0])
                    if ws == score:
                        #print "WS: " + str(ws)
                        #print "Raw: " + str(scores[WRITING_TYPE])
                        scores[WRITING_TYPE] = int(row[3])
                    elif rs == score:
                        #print "RS: " + str(rs)
                        #print "Raw: " + str(scores[READING_TYPE])                      
                        scores[READING_TYPE] = int(row[1])
                    elif ms == score:
                        #print "MS: " + str(ms)
                        #print "Raw: " + str(scores[READING_TYPE])                          
                        scores[MATH_TYPE] = int(row[2])                     
            self.section_scores = scores

    #String override method.
    def __str__(self):
        output = "Test ID: " + str(self.id) + endl
        output += "Total: " + str(self.total_score()) + endl
        output += "Writing: " + str(self.section_scores[WRITING_TYPE]) + endl
        output += "Reading: " + str(self.section_scores[READING_TYPE]) + endl
        output += "Math: " + str(self.section_scores[MATH_TYPE]) + endl
        return output


class Test_Summary(object):

    #This is the default constructor with all variables defined.
    def __init__(self, test_id):
        self.id = test_id
        self.reports = {}
        self.reports[MATH_TYPE] = Section_Summary(test_id, MATH_TYPE)
        self.reports[READING_TYPE] = Section_Summary(test_id, READING_TYPE)
        self.reports[WRITING_TYPE] = Section_Summary(test_id, WRITING_TYPE)

    #This returns the section summary for a corresponding section.
    def get_summary(self, section_type):
        return self.reports[section_type]

    def __str__(self):
        output = ("\nWRITING:" + endl)
        current_type = WRITING_TYPE
        output += str(self.get_summary(current_type))
        output += ("\nMATH:" + endl)
        current_type = MATH_TYPE
        output += str(self.get_summary(current_type))
        output += ("\nREADING:" + endl)
        current_type = READING_TYPE
        output += str(self.get_summary(current_type))
        return output

#Base Scored Section Class
class Section_Summary(object):

        #This is the default constructor with all variables defined.
    def __init__(self, test_id, section_type):
        self.id = test_id
        self.type = section_type
        self.qa = 0
        self.qm = 0
        self.qb = 0
        self.incorrect_questions = []

    def raw_score(self):
        return self.qa - round_rem(float(self.qm)/4)

    def size(self):
        return self.qa + self.qm + self.qb

    def add_miss(self):
        self.qm += 1

    def add_blank(self):
        self.qb += 1

    def add_answered(self):
        self.qa += 1

    def __str__(self):
        output = ("QA: " + str(self.qa) + endl)
        output += ("QM: " + str(self.qm) + endl)
        output += ("QB: " + str(self.qb) + endl)
        output += ("Raw Score: " + str(self.raw_score()) + endl)
        output += ("Missed Questions:" + str(self.incorrect_questions) + endl)
        return output