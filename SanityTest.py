import sys
sys.path.append('Library')
from Values import *
from Key import *
from Scored import *
from Summary import *
from Data import *
#from Graph import *  #commented out due to import clashing from user.py
from Console import *
from Class_Analytics import *
import shutil
import csv
import unittest

#class SetupTeardownError(Exception):

 #   def __init__(self, value):
  #      self.value = value

   # def __str__(self):
    #    return repr(self.value)

class SanityTest(unittest.TestCase):


    def setUp(self):
        # construct a test user here named dummy
        self.c = Console()
        self.name = "dummy"
       # print(self.c)
        #test new class
        res = self.c.process_commands('new_class ' + self.name)
        #print("res is: " + str(res))
        if (not res):
            print(self.c.error)
        else:     
            if(self.c.state == CLASS_STATE):
                ClassName = self.c.c.name
                #print ("Class "+ ClassName +" was created.")

    def tearDown(self):

        shutil.rmtree('./Users/dummy')

    def test_loadClass(self):
        #test load class
        res = self.c.process_commands('load_class ' + self.name)    
        self.assertEqual(res, True)  

    def test_newUser(self):
        #test load class
        res = self.c.process_commands('load_class ' + self.name)    
        self.assertEqual(res, True) 
        #test new student
        res = self.c.process_commands('new_student ' + self.name)
        self.assertEqual(res, True) 

    def test_loadUser(self):
        #test load class
        res = self.c.process_commands('load_class ' + self.name)    
        self.assertEqual(res, True) 
        #test new student
        res = self.c.process_commands('new_student ' + self.name)
        self.assertEqual(res, True) 
         #test load student
        res = self.c.process_commands('load_student ' + self.name)
        self.assertEqual(res, True)

    def test_createAnswerSheet(self):
         #test load class
        res = self.c.process_commands('load_class ' + self.name)    
        self.assertEqual(res, True) 
        #test new student
        res = self.c.process_commands('new_student ' + self.name)
        self.assertEqual(res, True) 
         #test load student
        res = self.c.process_commands('load_student ' + self.name)
        self.assertEqual(res, True)
        res = self.c.process_commands('answer_sheet GE30')  #create answer sheet test
        self.assertEqual(res, True)

    def test_gradeTest(self):
        #test load class
        res = self.c.process_commands('load_class ' + self.name)    
        self.assertEqual(res, True) 
        #test new student
        res = self.c.process_commands('new_student ' + self.name)
        self.assertEqual(res, True) 
         #test load student
        res = self.c.process_commands('load_student ' + self.name)
        self.assertEqual(res, True)
        res = self.c.process_commands('answer_sheet GE30')  #create answer sheet test
        #test grade test
        self.assertEqual(res, True)
        res = self.c.process_commands('grade GE30.csv')
        self.assertEqual(res, True)

    def test_saveUser(self):
        #test load class
        res = self.c.process_commands('load_class ' + self.name)    
        self.assertEqual(res, True) 
        #test new student
        res = self.c.process_commands('new_student ' + self.name)
        self.assertEqual(res, True) 
        #test load student
        res = self.c.process_commands('load_student ' + self.name)
        self.assertEqual(res, True)
        res = self.c.process_commands('answer_sheet GE30')  #create answer sheet test
        #test grade test
        self.assertEqual(res, True)
        res = self.c.process_commands('grade GE30.csv')
        self.assertEqual(res, True)
        res = self.c.process_commands('save')
        self.assertEqual(res, True)

    def test_graphReport(self):
        #test load class
        res = self.c.process_commands('load_class ' + self.name)    
        self.assertEqual(res, True) 
        #test new student
        res = self.c.process_commands('new_student ' + self.name)
        self.assertEqual(res, True) 
         #test load student
        res = self.c.process_commands('load_student ' + self.name)
        self.assertEqual(res, True)
        res = self.c.process_commands('answer_sheet GE30')  #create answer sheet test
        #test grade test
        self.assertEqual(res, True)
        res = self.c.process_commands('grade GE30.csv')
        self.assertEqual(res, True)
        # test graph report
        res = self.c.process_commands('graph_report')
        self.assertEqual(res, True)

    def test_sectionReport(self):
        #test load class
        res = self.c.process_commands('load_class ' + self.name)    
        self.assertEqual(res, True) 
        #test new student
        res = self.c.process_commands('new_student ' + self.name)
        self.assertEqual(res, True) 
         #test load student
        res = self.c.process_commands('load_student ' + self.name)
        self.assertEqual(res, True)
        res = self.c.process_commands('answer_sheet GE30')  #create answer sheet test
        #test grade test
        self.assertEqual(res, True)
        res = self.c.process_commands('grade GE30.csv')
        self.assertEqual(res, True)
        # test section report
        res = self.c.process_commands('section_report')
        self.assertEqual(res, True)

    def test_advancedReport(self):
        #test load class
        res = self.c.process_commands('load_class ' + self.name)    
        self.assertEqual(res, True) 
        #test new student
        res = self.c.process_commands('new_student ' + self.name)
        self.assertEqual(res, True) 
         #test load student
        res = self.c.process_commands('load_student ' + self.name)
        self.assertEqual(res, True)
        res = self.c.process_commands('answer_sheet GE30')  #create answer sheet test
        #test grade test
        self.assertEqual(res, True)
        res = self.c.process_commands('grade GE30.csv')
        self.assertEqual(res, True)
        # test advanced report
        res = self.c.process_commands('advanced_report')
        self.assertEqual(res, True)

    def test_simpleReport(self):
        #test load class
        res = self.c.process_commands('load_class ' + self.name)    
        self.assertEqual(res, True) 
        #test new student
        res = self.c.process_commands('new_student ' + self.name)
        self.assertEqual(res, True) 
         #test load student
        res = self.c.process_commands('load_student ' + self.name)
        self.assertEqual(res, True)
        res = self.c.process_commands('answer_sheet GE30')  #create answer sheet test
        #test grade test
        self.assertEqual(res, True)
        res = self.c.process_commands('grade GE30.csv')
        self.assertEqual(res, True)
        # test simple report
        res = self.c.process_commands('simple_report')
        self.assertEqual(res, True)
    '''

    def test_autoGrader(self):
        #Autograde the dummy test with the test user's data
        mkdir("../../testfolder")
         #test load class
        res = self.c.process_commands('load_class ' + self.name)    
        self.assertEqual(res, True) 
        #test new student
        res = self.c.process_commands('new_student ' + self.name)
        self.assertEqual(res, True) 
         #test load student
        res = self.c.process_commands('load_student ' + self.name)
        self.assertEqual(res, True)
        res = self.c.process_commands('answer_sheet GE30')  #create answer sheet test
        #test grade test
        self.assertEqual(res, True)
        res = self.c.process_commands('grade GE30.csv')
        self.assertEqual(res, True)


        shutil.copy(user_directory(self.name) + DIR_SEP + 'GE30.csv', "../../testfolder" + DIR_SEP + self.name + ".csv")

        foldername = "../../testfolder"
        if file_exists(foldername):
          list_of_tests = os.listdir(foldername)
          for filename in list_of_tests:
              if ".csv" in filename:
                  pa = parse_answers(foldername + DIR_SEP + filename)
                  name = pa.name
                  if name == None or name not in list_users_array():
                      print ("Error", 'Student name not found. ' + filename + ' was unable to be graded.') 
                  else:
                      self.c.process_commands('load_student ' + name)
                      self.c.user.grade(pa)
                      self.c.process_commands('save')




        rmdir("../../testfolder")
        self.count += 1
    '''

    def test_classAnalytics(self):
        #Test the functionality of class analytics. Should be isolated from other users, and class should only include the test user. Or we can run classAnalytics, but only have the assertion statement check for the test user we created in setup()
        #test load class
        res = self.c.process_commands('load_class ' + self.name)    
        self.assertEqual(res, True) 
        #test new student
        res = self.c.process_commands('new_student ' + self.name)
        self.assertEqual(res, True) 
         #test load student
        res = self.c.process_commands('load_student ' + self.name)
        self.assertEqual(res, True)
        res = self.c.process_commands('answer_sheet GE30')  #create answer sheet test
        #test grade test
        self.assertEqual(res, True)
        res = self.c.process_commands('grade GE30.csv')
        self.assertEqual(res, True)

        
        a = Analytics(self.c.c.name)
        a.report()
        dirc = user_directory('', self.c.c.name)
        self.assertEqual(file_exists(dirc + DIR_SEP + 'analytics.html'), True)




suite = unittest.TestLoader().loadTestsFromTestCase(SanityTest)
unittest.TextTestRunner(verbosity=2).run(suite)
