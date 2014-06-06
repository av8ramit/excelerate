import sys
sys.path.append('Library')
from Values import *
from Key import *
from Scored import *
from Summary import *
from Data import *
from Graph import *
from Console import *
from Class_Analytics import *
import shutil
import csv
import unittest

class SetupTeardownError(Exception):

    def __init__(self, value):
        self.value = value

    def __str__(self):
        return repr(self.value)

class SanityTest(unittest.TestCase):


    def setUp(self):
        # construct a test user here named dummy
        self.c = Console()
        self.count = 0
        self.total = 1
        self.passed = self.total
        self.name = "dummy"
        self.name2 = "dummy2"
        res = self.c.process_commands('new_student ' + self.name)        
        if (not res):
            raise SetupTeardownError("Failed to set up.")
        res2 = self.c.process_commands('new_student ' + self.name2)        
        if (not res2):
            raise SetupTeardownError("Failed to set up.")

    def tearDown(self):
        # delete a test user here along with all data related to it
        res = self.c.process_commands('delete_student ' + self.name)
        if (not res):
            raise SetupTeardownError("Failed to tear down. Manually reset the environment before testing.")
        res2 = self.c.process_commands('delete_student ' + self.name2)        
        if (not res2):
            raise SetupTeardownError("Failed to tear down. Manually reset the environment before testing.")
        print ("TEST PASSED")

    def testLoadUser(self):
        #Test the loading of a user
        #print ("Starting Load User Test")
        res = self.c.process_commands('load_student ' + self.name2)
        if (not res):
            raise SetupTeardownError("Load Student Failed Internally.")
        res2 = self.c.process_commands('load_student ' + self.name)
        if (not res2):
            raise SetupTeardownError("Load Student Failed Internally.")
        self.count += 1
        #print ("Ending Load User Test")

    def testCreateAnswerSheet(self):
        #Create an answer sheet to the dummy test created above
        res = self.c.process_commands('load_student ' + self.name2)
        if (not res):
            raise SetupTeardownError("Load Student Failed Internally.")

        res = self.c.process_commands('answer_sheet ' + "10_09")
        if (not res):
            raise SetupTeardownError("Answer Sheet Failed Internally.")

        res = self.c.process_commands('answer_sheet ' + "12_09")
        if (res):
            raise SetupTeardownError("Answer Sheet Didn't Fail when it should have internally.")
        self.count += 1

    def testAutoGrader(self):
        #Autograde the dummy test with the test user's data
        mkdir("../../testfolder")
        res = self.c.process_commands('load_student ' + self.name2)

        if (not res):
            raise SetupTeardownError("Load Student Failed Internally.")

        res = self.c.process_commands('answer_sheet ' + "10_09")
        if (not res):
            raise SetupTeardownError("Answer Sheet Failed Internally.")

        shutil.copy(user_directory(self.name2) + DIR_SEP + '10_09.csv', "../../testfolder" + DIR_SEP + self.name2 + ".csv")

        res = self.c.process_commands('load_student ' + self.name)
        if (not res):
            raise SetupTeardownError("Load Student Failed Internally.")

        res = self.c.process_commands('answer_sheet ' + "10_09")
        if (not res):
            raise SetupTeardownError("Answer Sheet Failed Internally.")

        shutil.copy(user_directory(self.name2) + DIR_SEP + '10_09.csv', "../../testfolder" + DIR_SEP + self.name + ".csv")

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

    def testSaveChanges(self):
        #Check the functionality of this
        res = self.c.process_commands('load_student ' + self.name)

        if (not res):
            raise SetupTeardownError("Load Student Failed Internally.")

        res = self.c.process_commands('answer_sheet ' + "10_09")
        if (not res):
            raise SetupTeardownError("Answer Sheet Failed Internally.")

        res = self.c.process_commands('grade ' + "10_09.csv")
        if (not res):
            raise SetupTeardownError("Grade Failed Internally.")

        res = self.c.process_commands('save')
        if (not res):
            raise SetupTeardownError("Save Failed Internally.")
        self.count += 1
    
    def testAdvancedReport(self):
        #Test the data sent to the html creator. Don't actually launch any reports
        res = self.c.process_commands('load_student ' + self.name)

        if (not res):
            raise SetupTeardownError("Load Student Failed Internally.")

        res = self.c.process_commands('answer_sheet ' + "10_09")
        if (not res):
            raise SetupTeardownError("Answer Sheet Failed Internally.")

        for i in range(0, random_number(10)):
            res = self.c.process_commands('grade ' + "10_09.csv")
            if (not res):
                raise SetupTeardownError("Grade Failed Internally.")

        res = self.c.process_commands('save')
        if (not res):
            raise SetupTeardownError("Save Failed Internally.")

        res = self.c.process_commands("advanced_report")
        if (not res):
            raise SetupTeardownError("Simple Report Failed Internally.")
        self.count += 1

    """
    def testSimpleReport(self):
        #Same as above
        pass

    def testSectionReport(self):
        #Same as above
        pass

    def testGraphsReport(self):
        #Same as above
        pass
    """

    def testClassAnalytics(self):
        #Test the functionality of class analytics. Should be isolated from other users, and class should only include the test user. Or we can run classAnalytics, but only have the assertion statement check for the test user we created in setup()
        res = self.c.process_commands('load_student ' + self.name)

        if (not res):
            raise SetupTeardownError("Load Student Failed Internally.")

        res = self.c.process_commands('answer_sheet ' + "10_09")
        if (not res):
            raise SetupTeardownError("Answer Sheet Failed Internally.")

        res = self.c.process_commands('grade ' + "10_09.csv")
        if (not res):
            raise SetupTeardownError("Grade Failed Internally.")

        res = self.c.process_commands('save')
        if (not res):
            raise SetupTeardownError("Save Failed Internally.")

        res = self.c.process_commands('load_student ' + self.name2)

        if (not res):
            raise SetupTeardownError("Load Student Failed Internally.")

        res = self.c.process_commands('answer_sheet ' + "10_09")
        if (not res):
            raise SetupTeardownError("Answer Sheet Failed Internally.")

        res = self.c.process_commands('grade ' + "10_09.csv")
        if (not res):
            raise SetupTeardownError("Grade Failed Internally.")

        res = self.c.process_commands('save')
        if (not res):
            raise SetupTeardownError("Save Failed Internally.")

        a = Analytics()
        a.report()
        self.count += 1

    """def testCollegeTracker(self):
        pass
        """


