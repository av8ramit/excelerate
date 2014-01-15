####################################################################################################################################################  
#                                                                                                                                                  #
# This file has been generated by Amit Patankar:                                                                                                   #
#     Created by              : amit.patankar                                                                                                      #    
#     Created on              : 14-07-2013                                                                                                         #
#     Directory               : /Desktop/                                                                                                          #
#     Purpose                 : This structure holds the attributes of each Answer Sheet.                                                          #
#                                                                                                                                                  #
####################################################################################################################################################

from Values import *
from Key import *
from Scored import *
from Summary import *
from Data import *
from Graph import *
import csv

#Base Section Class
class User(object):

    #This is the default constructor with all variables defined.
    def __init__(self, name):
        self.name = name
        self.tests_taken = [] #array of scored tests for data analysis
        self.data = Data_Holder()
    
    def build(self):
        mkdir(self.directory())
        self.save_user()

    def directory(self):
        return "Users" + DIR_SEP + self.name

    def grade(self, answers):
        t = Test(answers.id)
        ts = t.grade(answers)
        ss = Score_Summary(ts)
        print (ss)
        sections = {}
        sections[WRITING_TYPE] = ts.reports[WRITING_TYPE].incorrect_questions
        sections[MATH_TYPE] = ts.reports[MATH_TYPE].incorrect_questions
        sections[READING_TYPE] = ts.reports[READING_TYPE].incorrect_questions
        st = Scored_Test(answers.id)
        st.recreate(sections)
        #put the scored test in the history page after it has been graded
        self.tests_taken.append(st)
        #add this new test to data sections
        self.stats_from_test(st)


    def save_user(self):
        FILE = open(self.directory() + DIR_SEP + self.name + ".txt", "w")
        lines = []
        lines.append("Name:" + self.name + endl + endl)
        for test in self.tests_taken:
            lines.append(str(test))
        FILE.writelines(lines)          
        FILE.close()


    def recreate_user(self, filename):
        with open(filename) as f:
            lines = f.readlines()
            assert(self.name in lines[0]) #verifies name
            for line in lines:
                line = line.strip()
                if line == '':
                    continue
                elif 'TEST_ID' in line:
                    test_id = line.split(' ')[1]
                    sections = {}
                    current_test = Scored_Test(test_id)
                elif 'WRITING:' in line:
                    current_TYPE = WRITING_TYPE
                elif 'MATH:' in line:
                    current_TYPE = MATH_TYPE
                elif 'READING:' in line:
                    current_TYPE = READING_TYPE
                elif 'Missed Questions:' in line:
                    data = string_to_array(line.split(":")[1])
                    sections[current_TYPE] = data
                elif SECTION_SEP in line:
                    current_test.recreate(sections)
                    sections = {}
                    self.tests_taken.append(current_test)
        for test in self.tests_taken:
            self.stats_from_test(test)



    def stats_from_test(self, test):
        with open(test.test_id + DIR_SEP + KEYFILE, 'rU') as f:
            reader = csv.reader(f)
            key = {}
            for row in reader:
                if row != KEY_VECTOR or row[0] == '':
                    index = int(row[0])
                    section_type = int(row[1])
                    size = int(row[2])
                    key[index] = (section_type, size)
        for index in key.keys():
            self.stats_from_file(test, key, index)


    def stats_from_file(self, test, key, index):
        section_type = key[index][0]
        if not file_exists(test.test_id + DIR_SEP + "Section " + str(index) + CSV):
            return
        ifile  = open(test.test_id + DIR_SEP + "Section " + str(index) + CSV, "rU")
        reader = csv.reader(ifile)

        for row in reader:
            if row != LABEL_VECTOR or row[0] == '':
                number = int(row[NUMBER_INDEX])
                difficulty = int(row[DIFFICULTY_INDEX])
                qtype = row[TYPE_INDEX]
                if index_exists(test.missed_questions_index, index) and index_exists(test.missed_questions_index[index], number):
                    attempt = test.missed_questions_index[index][number]
                    if attempt == '?':
                        self.data.data[section_type].stats["L" + str(difficulty)].add_blank()
                        self.data.data[section_type].stats[qtype].add_blank()
                        test.data.data[section_type].stats["L" + str(difficulty)].add_blank()
                        test.data.data[section_type].stats[qtype].add_blank()
                        #complete data processing
                        #add the level and type blanks
                    else:
                        self.data.data[section_type].stats["L" + str(difficulty)].add_miss()
                        self.data.data[section_type].stats[qtype].add_miss()
                        test.data.data[section_type].stats["L" + str(difficulty)].add_miss()
                        test.data.data[section_type].stats[qtype].add_miss()
                else:
                    self.data.data[section_type].stats["L" + str(difficulty)].add_correct()
                    self.data.data[section_type].stats[qtype].add_correct()
                    test.data.data[section_type].stats["L" + str(difficulty)].add_correct()
                    test.data.data[section_type].stats[qtype].add_correct()

        ifile.close()

    def average_scores(self):
        writing_score = 0
        reading_score = 0
        math_score = 0
        total_score = 0
        for test in self.tests_taken:
            writing_score += test.score_summary.section_scores[WRITING_TYPE]
            reading_score += test.score_summary.section_scores[READING_TYPE]
            math_score += test.score_summary.section_scores[MATH_TYPE]
        total_score = (writing_score + reading_score + math_score) // len(self.tests_taken)
        reading_score = reading_score // len(self.tests_taken)
        writing_score = writing_score // len(self.tests_taken)
        math_score = math_score // len(self.tests_taken)
        return [total_score, reading_score, writing_score, math_score]

    def reset_account(self):
        self.tests_taken = [] #array of scored tests for data analysis
        self.data = Data_Holder()
        self.save_user()

    def simple_HTML(self):
        FILE = open(self.directory() + DIR_SEP + "simple_report" + ".html", "w")
        lines = []

        index = 1
        scores = self.average_scores()
        s1 = []
        #calculate all scores
        for test in self.tests_taken:
            s1.append([index,test.score_summary.total_score()])
            index += 1

        #graph js
        g = Graph("Overall Score Performance", 1, s1)

        #HTML opener
        lines.append('<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.1//EN" "http://www.w3.org/TR/xhtml11/DTD/xhtml11.dtd">' + endl)
        lines.append('<html xmlns="http://www.w3.org/1999/xhtml">' + endl)
        lines.append('<head>')
        lines.append('<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />' + endl)
        lines.append('<link rel="stylesheet" type="text/css" href="../../HTML/style.css" />' + endl)
        lines.append('<title>Simple Score Report</title>' + endl)
        lines += g.head()
        lines.append('</head>' + endl)
        lines.append('<body>' + endl)
        lines.append('<div id="page">' + endl)
        lines.append('<div id="header">' + endl)
        lines.append('<img src="../../HTML/Mini Logo.png" width="35%" alt="Excelerate" />' + endl)
        lines.append('</div>' + endl)
        lines.append('</div>' + endl)
        lines.append('<div id="content">' + endl)
        lines.append('<div id="container">' + endl)
        lines.append('<div id="main">' + endl)
        lines.append('<div id="menu">' + endl)
        lines.append('<h2 style="text-align:center;">Simple Report: ' + self.name + '</h2>' + endl)
        lines.append('</div>' + endl)
        lines.append('<div id="text">' + endl)
        

        #Qualitative Performance
        lines.append('<h1>Qualitative Performance</h1>' + endl)
        lines.append('<p><b>Overall Aptitude:</b><font color = "' + overall_qualitative_color(scores[0]) + '"> ' + overall_qualitative(scores[0]) + '</font></p>' + endl)
        lines.append('<p><b>Writing Performance:</b><font color = "' + qualitative_color(scores[2]) + '"> ' + qualitative(scores[2]) + '</font></p>' + endl)
        lines.append('<p><b>Reading Performance:</b><font color = "' + qualitative_color(scores[1]) + '"> ' + qualitative(scores[1]) + '</font></p>' + endl)
        lines.append('<p><b>Math Performance:</b><font color = "' + qualitative_color(scores[3]) + '"> ' + qualitative(scores[3]) + '</font></p>' + endl)
        lines.append('<p><b>Essay Performance:</b> Unknown</p>' + endl)
        lines.append('<p><i>Here are the details regarding the scores. Average scores are between 500 to 600. All scores above average are recorded as proficient and all scores below are noted as poor. Unknown scores have no records.</i></p>' + endl)
        lines.append('<hr color="#BBBBBB" size="2" width="100%">' + endl)

        #Average Results
        lines.append('<h1>Average Results</h1>' + endl)
        lines.append('<p><b>Total Score:</b><font color = "' + overall_qualitative_color(scores[0]) + '">  ' + str(scores[0]) + '/2400</font></p>' + endl)
        lines.append('<p><b>Average Writing Score:</b><font color = "' + qualitative_color(scores[2]) + '">  ' + str(scores[2]) + '/800</font></p>' + endl)
        lines.append('<p><b>Average Reading Score:</b><font color = "' + qualitative_color(scores[1]) + '">  ' + str(scores[1]) + '/800</font></p>' + endl)
        lines.append('<p><b>Average Math Score:</b><font color = "' + qualitative_color(scores[3]) + '">  ' + str(scores[3]) + '/800</font></p>' + endl)
        lines.append('<p><b>Average Essay Score:</b> ??/12</p>' + endl)
        lines.append('<p><b>Tests Taken:</b> ' + str(len(self.tests_taken)) + '</p>' + endl)
        lines.append('<hr color="#BBBBBB" size="2" width="100%">' + endl)

        #Previous Test History
        """lines.append('<h1>Previous Test History</h1>' + endl)
        for test in self.tests_taken:
            lines.append('<p><b>Test ID:</b> ' + test.test_id + '</p>' + endl)
            lines.append('<p><b>Total:</b> ' + str(test.score_summary.total_score())+'</p>' + endl)
            lines.append('<p><b>Writing:</b> ' + str(test.score_summary.section_scores[WRITING_TYPE]) +'</p>' + endl)
            lines.append('<p><b>Reading:</b> ' + str(test.score_summary.section_scores[READING_TYPE]) +'</p>' + endl)
            lines.append('<p><b>Math:</b> ' + str(test.score_summary.section_scores[MATH_TYPE]) +'</p>' + endl)
            lines.append('<br>' + endl)
        lines.append('<hr color="#BBBBBB" size="2" width="100%">' + endl)"""

        #Overall Graph
        lines += g.html()

        #Footer
        lines.append('<br>' + endl)
        lines.append('</div>' + endl)
        lines.append('</div>' + endl)
        lines.append('</div>' + endl)
        lines.append('<div class="clear"></div>' + endl)
        lines.append('<div id="footer">' + endl)
        lines.append('<p><a>' + self.name + ' Simple Report</a></p>' + endl)
        lines.append('</div>' + endl)
        lines.append('</div>' + endl)
        lines += g.body()
        lines.append('</body>' + endl)
        lines.append('</html>' + endl)
        lines.append(endl)

        FILE.writelines(lines)
        FILE.close()

    def type_HTML(self, section_type):
        section_type_name = section_name(section_type)
        FILE = open(self.directory() + DIR_SEP + section_type_name.lower() + "_report" + ".html", "w")
        lines = []

        index = 1
        graph_index = 1
        scores = self.average_scores()
        s1 = []
        graphs = []
        #calculate all scores
        for test in self.tests_taken:
            s1.append([index,test.score_summary.total_score()])
            index += 1
        
        g = Graph(section_type_name + " Score Performance", graph_index, s1)
        type_dict = section_type_dict(section_type)

        for i in range(1, len(type_dict)):
            key = section_type_name[0] + str(i)
            data = []
            graph_index += 1
            for test in self.tests_taken:
                data.append(test.data.data[section_type].stats[key].c)

            graphs.append(Graph(type_dict[key], graph_index, data))




        #HTML opener
        lines.append('<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.1//EN" "http://www.w3.org/TR/xhtml11/DTD/xhtml11.dtd">' + endl)
        lines.append('<html xmlns="http://www.w3.org/1999/xhtml">' + endl)
        lines.append('<head>')
        lines.append('<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />' + endl)
        lines.append('<link rel="stylesheet" type="text/css" href="../../HTML/style.css" />' + endl)
        lines.append('<title>' + section_type_name + ' Score Report</title>' + endl)
        lines += g.head()
        lines.append('</head>' + endl)
        lines.append('<body>' + endl)
        lines.append('<div id="page">' + endl)
        lines.append('<div id="header">' + endl)
        lines.append('<img src="../../HTML/Mini Logo.png" width="35%" alt="Excelerate" />' + endl)
        lines.append('</div>' + endl)
        lines.append('</div>' + endl)
        lines.append('<div id="content">' + endl)
        lines.append('<div id="container">' + endl)
        lines.append('<div id="main">' + endl)
        lines.append('<div id="menu">' + endl)
        lines.append('<h2 style="text-align:center;">' + section_type_name + SPACE + 'Analytics Report: ' + self.name + '</h2>' + endl)
        lines.append('</div>' + endl)
        lines.append('<div id="text">' + endl)
        


        #Average Results
        lines.append('<h1>' + section_type_name + ' Analytics</h1>' + endl)
        lines.append('<hr color="#BBBBBB" size="2" width="100%">' + endl)


        #Overall Graph
        lines += g.html()
        lines.append("<p>This is your performance in the " + section_type_name + " section of the last " + str(len(self.tests_taken)) + " tests you have taken. The more comprehensive analysis of questions correct in each type is found below.</p>")


        #Average Results
        lines.append('<h1>Question Type Analytics</h1>' + endl)
        lines.append('<hr color="#BBBBBB" size="2" width="100%">' + endl)

        #Print the type analysis as well
        i = 1
        for graph in graphs:
            lines += graph.html()
            lines.append('<p><b><font color = "' + self.data.data[section_type].stats[section_type_name[0] + str(i)].color() +'">' + type_dict[section_type_name[0] + str(i)] + "</b> " + str(self.data.data[section_type].stats[section_type_name[0]+str(i)]) + '</p>')
            i+=1 
            lines.append('<hr color="#4169EF" size="1" width="90%">' + endl)
            #lines.append("<br>" + endl)

        #Footer
        lines.append('<br>' + endl)
        lines.append('</div>' + endl)
        lines.append('</div>' + endl)
        lines.append('</div>' + endl)
        lines.append('<div class="clear"></div>' + endl)
        lines.append('<div id="footer">' + endl)
        lines.append('<p><a>' + self.name + SPACE + section_type_name + SPACE +' Report</a></p>' + endl)
        lines.append('</div>' + endl)
        lines.append('</div>' + endl)
        lines += g.body()
        lines.append('</body>' + endl)
        lines.append('</html>' + endl)
        lines.append(endl)

        FILE.writelines(lines)
        FILE.close()



    def advanced_HTML(self):

        FILE = open(self.directory() + DIR_SEP + "advanced_report" + ".html", "w")
        lines = []

        scores = self.average_scores()

        #HTML opener
        lines.append('<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.1//EN" "http://www.w3.org/TR/xhtml11/DTD/xhtml11.dtd">' + endl)
        lines.append('<html xmlns="http://www.w3.org/1999/xhtml">' + endl)
        lines.append('<head>')
        lines.append('<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />' + endl)
        lines.append('<link rel="stylesheet" type="text/css" href="../../HTML/style.css" />' + endl)
        lines.append('<title>Advanced Score Report</title>' + endl)
        lines.append('</head>' + endl)
        lines.append('<body>' + endl)
        lines.append('<div id="page">' + endl)
        lines.append('<div id="header">' + endl)
        lines.append('<img src="../../HTML/Mini Logo.png" width="35%" alt="Excelerate" />' + endl)
        lines.append('</div>' + endl)
        lines.append('</div>' + endl)
        lines.append('<div id="content">' + endl)
        lines.append('<div id="container">' + endl)
        lines.append('<div id="main">' + endl)
        lines.append('<div id="menu">' + endl)
        lines.append('<h2 style="text-align:center;">Advanced Report: ' + self.name + '</h2>' + endl)
        lines.append('</div>' + endl)
        lines.append('<div id="text">' + endl)
            

        #Average Results
        lines.append('<h1>Average Results</h1>' + endl)
        lines.append('<p><b>Total Score:</b><font color = "' + overall_qualitative_color(scores[0]) + '">  ' + str(scores[0]) + '/2400</font></p>' + endl)
        lines.append('<p><b>Average Writing Score:</b><font color = "' + qualitative_color(scores[2]) + '">  ' + str(scores[2]) + '/800</font></p>' + endl)
        lines.append('<p><b>Average Reading Score:</b><font color = "' + qualitative_color(scores[1]) + '">  ' + str(scores[1]) + '/800</font></p>' + endl)
        lines.append('<p><b>Average Math Score:</b><font color = "' + qualitative_color(scores[3]) + '">  ' + str(scores[3]) + '/800</font></p>' + endl)
        lines.append('<p><b>Average Essay Score:</b> ??/12</p>' + endl)
        lines.append('<p><b>Tests Taken:</b> ' + str(len(self.tests_taken)) + '</p>' + endl)
        lines.append('<hr color="#BBBBBB" size="2" width="100%">' + endl)



        #Section Analysis
        lines.append(endl)
        lines.append("<h1>Section Performance Analysis</h1>" + endl)
        lines.append('<p><font color = "#093175">Type: Total Questions | Questions Correct | Questions Missed | Questions Blank</font></p><br>' + endl)
        lines.append(endl)

        #Writing Analytics
        lines.append("<h3><i>Writing Analytics:</i></h3>" + endl)
        for i in range(1, WRITING_TYPES + 1):
            lines.append('<p><b><font color = "' + self.data.data[WRITING_TYPE].stats["W"+str(i)].color() +'">' + WRITING_TYPE_DICT["W" + str(i)] + '</b> ' + str(self.data.data[WRITING_TYPE].stats["W"+str(i)]) + '</p>')
            lines.append(endl)
        lines.append('<hr color="#4169EF" size="1" width="90%">' + endl)
        lines.append("<br>" + endl)     

        #Reading Analytics
        lines.append("<h3><i>Reading Analytics:</i></h3>" + endl)
        for i in range(1, READING_TYPES + 1):
            lines.append('<p><b><font color = "' + self.data.data[READING_TYPE].stats["R"+str(i)].color() +'">' + READING_TYPE_DICT["R" + str(i)] + "</b> " + str(self.data.data[READING_TYPE].stats["R"+str(i)]) + '</p>')
            lines.append(endl)  
        lines.append('<hr color="#4169EF" size="1" width="90%">' + endl)
        lines.append("<br>" + endl)

        #Math Analytics
        lines.append("<h3><i>Math Analytics:</i></h3>" + endl)
        for i in range(1, MATH_TYPES + 1):
            lines.append('<p><b><font color = "' + self.data.data[MATH_TYPE].stats["M"+str(i)].color() +'">' + MATH_TYPE_DICT["M" + str(i)] + "</b> " + str(self.data.data[MATH_TYPE].stats["M"+str(i)]) + '</p>')
            lines.append(endl)  
        lines.append("<br>" + endl) 
        lines.append('<hr color="#BBBBBB" size="2" width="100%">' + endl)

        #Footer
        lines.append('<br>' + endl)
        lines.append('</div>' + endl)
        lines.append('</div>' + endl)
        lines.append('</div>' + endl)
        lines.append('<div class="clear"></div>' + endl)
        lines.append('<div id="footer">' + endl)
        lines.append('<p><a>' + self.name + ' Advanced Report</a></p>' + endl)
        lines.append('</div>' + endl)
        lines.append('</div>' + endl)


        lines.append('</body>' + endl)
        lines.append('</html>' + endl)
        lines.append(endl)

        FILE.writelines(lines)
        FILE.close()


    def graph_HTML(self):
        graphs = []
        s1 = []
        writing_scores = []
        reading_scores = []
        math_scores = []
        graph_index = 1
        index = 1

        #calculate all scores
        for test in self.tests_taken:
            s1.append([index,test.score_summary.total_score()])
            writing_scores.append([index, test.score_summary.section_scores[WRITING_TYPE]])
            reading_scores.append([index, test.score_summary.section_scores[READING_TYPE]])
            math_scores.append([index, test.score_summary.section_scores[MATH_TYPE]])
            index += 1

        #graph js
        g = Graph("Overall Score Performance", graph_index, s1)
        graph_index += 1
        wg = Graph("Writing Score Performance", graph_index, writing_scores)
        graph_index += 1
        rg = Graph("Reading Score Performance", graph_index, reading_scores)
        graph_index += 1
        mg = Graph("Math Score Performance", graph_index, math_scores)
        graph_index += 1
        graphs.append(g)
        graphs.append(wg)
        graphs.append(rg)
        graphs.append(mg)


        FILE = open(self.directory() + DIR_SEP + "graph_report" + ".html", "w")
        lines = []

        scores = self.average_scores()

        #HTML opener
        lines.append('<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.1//EN" "http://www.w3.org/TR/xhtml11/DTD/xhtml11.dtd">' + endl)
        lines.append('<html xmlns="http://www.w3.org/1999/xhtml">' + endl)
        lines.append('<head>')
        lines.append('<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />' + endl)
        lines.append('<link rel="stylesheet" type="text/css" href="../../HTML/style.css" />' + endl)
        lines.append('<title>Graph Report</title>' + endl)
        lines += g.head()
        lines.append('</head>' + endl)
        lines.append('<body>' + endl)
        lines.append('<div id="page">' + endl)
        lines.append('<div id="header">' + endl)
        lines.append('<img src="../../HTML/Mini Logo.png" width="35%" alt="Excelerate" />' + endl)
        lines.append('</div>' + endl)
        lines.append('</div>' + endl)
        lines.append('<div id="content">' + endl)
        lines.append('<div id="container">' + endl)
        lines.append('<div id="main">' + endl)
        lines.append('<div id="menu">' + endl)
        lines.append('<h2 style="text-align:center;">Graph Report: ' + self.name + '</h2>' + endl)
        lines.append('</div>' + endl)
        lines.append('<div id="text">' + endl)
            

        #Average Results
        lines.append('<h1>Score Graphs</h1>' + endl)
        lines.append('<hr color="#BBBBBB" size="2" width="100%">' + endl)

        #Graph js
        for graph in graphs:
            lines += graph.html()
            lines.append('<br><hr color="#4169EF" size="1" width="90%">' + endl)
            lines.append(endl)




        #Footer
        lines.append('<br>' + endl)
        lines.append('</div>' + endl)
        lines.append('</div>' + endl)
        lines.append('</div>' + endl)
        lines.append('<div class="clear"></div>' + endl)
        lines.append('<div id="footer">' + endl)
        lines.append('<p><a>' + self.name + ' Advanced Report</a></p>' + endl)
        lines.append('</div>' + endl)
        lines.append('</div>' + endl)

        #scripts
        lines += g.body()


        lines.append('</body>' + endl)
        lines.append('</html>' + endl)
        lines.append(endl)

        FILE.writelines(lines)
        FILE.close()


    def simple_report(self):
        FILE = open(self.directory() + DIR_SEP + "simple_report" + ".txt", "w")
        lines = []

        #Name
        line = "Name: " + self.name  + endl
        lines.append(line)
        lines.append(endl)
        lines.append(SECTION_SEP)

        #Scores
        scores = self.average_scores()
        lines.append(endl)
        lines.append("Scores:" + endl)
        lines.append("Average Total Score: " + str(scores[0]) + "/2400" + endl)
        lines.append("Average Writing Score: " + str(scores[2]) + "/800" + endl)
        lines.append("Average Reading Score: " + str(scores[1]) + "/800" + endl)
        lines.append("Average Math Score: " + str(scores[3]) + "/800" + endl)
        lines.append("Average Essay Score: " + "??/12" + endl)
        lines.append(endl)
        lines.append("Tests Taken: " + str(len(self.tests_taken)))
        lines.append(endl)
        lines.append(SECTION_SEP)
        lines.append(endl + endl)

        for test in self.tests_taken:
            lines.append(str(test.score_summary))
            lines.append(endl)

        FILE.writelines(lines)
        FILE.close()


    def advanced_report(self):
        FILE = open(self.directory() + DIR_SEP + "advanced_report" + ".txt", "w")
        lines = []

        #Name
        line = "Name: " + self.name  + endl
        lines.append(line)
        lines.append(endl)
        lines.append(SECTION_SEP)

        #Scores
        scores = self.average_scores()
        lines.append(endl)
        lines.append("Scores:" + endl)
        lines.append("Average Total Score: " + str(scores[0]) + "/2400" + endl)
        lines.append("Average Writing Score: " + str(scores[2]) + "/800" + endl)
        lines.append("Average Reading Score: " + str(scores[1]) + "/800" + endl)
        lines.append("Average Math Score: " + str(scores[3]) + "/800" + endl)
        lines.append("Average Essay Score: " + "??/12" + endl)
        lines.append(endl)
        lines.append("Tests Taken: " + str(len(self.tests_taken)))
        lines.append(endl)
        lines.append(SECTION_SEP)

        #Section Analysis
        lines.append(endl)
        lines.append("Section Performance Analysis:" + endl)
        lines.append("Type: Total Questions | Questions Correct | Questions Missed | Questions Blank" + endl)
        lines.append(endl)
        lines.append( "_______" + endl + endl)
        
        lines.append("Writing Analytics:" + endl)
        for i in range(1, WRITING_TYPES + 1):
            lines.append(WRITING_TYPE_DICT["W" + str(i)] + ": " + str(self.data.data[WRITING_TYPE].stats["W"+str(i)]))
            lines.append(endl)
        lines.append( "_______" + endl + endl)      

        lines.append("Math Analytics:" + endl)
        for i in range(1, MATH_TYPES + 1):
            lines.append(MATH_TYPE_DICT["M" + str(i)] + ": " + str(self.data.data[MATH_TYPE].stats["M"+str(i)]))
            lines.append(endl)
        lines.append( "_______" + endl + endl)
        
        lines.append("Reading Analytics:" + endl)
        for i in range(1, READING_TYPES + 1):
            lines.append(READING_TYPE_DICT["R" + str(i)] + ": " + str(self.data.data[READING_TYPE].stats["R"+str(i)]))
            lines.append(endl)

        lines.append(SECTION_SEP)

        #Difficulty Analysis
        lines.append(endl)
        lines.append("Difficulty Analytics:" + endl)
        lines.append(endl)
        lines.append("Writing:" + endl)
        for i in range(1,6):
            lines.append("Level " + str(i) + ": " + str(self.data.data[WRITING_TYPE].stats["L" + str(i)]))
            lines.append(endl)
        lines.append( "_______" + endl + endl)

        lines.append(endl)
        lines.append("Math:" + endl)
        for i in range(1,6):
            lines.append("Level " + str(i) + ": " + str(self.data.data[MATH_TYPE].stats["L" + str(i)]))
            lines.append(endl)
        lines.append( "_______" + endl + endl)

        lines.append(endl)
        lines.append("Reading:" + endl)
        for i in range(1,6):
            lines.append("Level " + str(i) + ": " + str(self.data.data[READING_TYPE].stats["L" + str(i)]))
            lines.append(endl)

        lines.append(endl)

        FILE.writelines(lines)
        FILE.close()




