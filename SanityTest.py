import sys
sys.path.append('Library')
from Values import *
from Key import *
from Scored import *
from Summary import *
from Data import *
from Graph import *
from Console import *
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
        name = "dummy"
        print(self.c)
        res = self.c.process_commands('new_student ' + name)
        print(self.c.error)
        if (not res):
            raise SetupTeardownError("Failed to set up.")
        else:     
            var = StringVar()
            if(c.state == LOAD_STATE):
                UserName = c.user.name
                var.set(UserName)
            print ("User was created.")

    def tearDown(self):
        # delete a test user here along with all data related to it
        name = "dummy"
        res = self.c.process_commands('delete_student ' + name)
        print ("User was deleted.")
        if (not res):
            raise SetupTeardownError("Failed to tear down. Manually reset the environment before testing.")


    def testLoadUser(self):
        #Test the loading of a user
        self.c.process_commands('load_student dummy')

    """def testImportData(self):
        #test importing test data
        pass

    def testCreateTest(self):
         #Create a dummy test
         pass

    def testCreateAnswerSheet(self):
        #Create an answer sheet to the dummy test created above
        pass

    def testAutoGrader(self):
        #Autograde the dummy test with the test user's data
        pass

    def testSaveChanges(self):
        #Check the functionality of this
        pass

    def testSimpleReport(self):
        #Test the data sent to the html creator. Don't actually launch any reports
        pass

    def testAdvancedReport(self):
        #Same as above
        pass

    def testSectionReport(self):
        #Same as above
        pass

    def testGraphsReport(self):
        #Same as above
        pass

    def testClassAnalytics(self):
        #Test the functionality of class analytics. Should be isolated from other users, and class should only include the test user. Or we can run classAnalytics, but only have the assertion statement check for the test user we created in setup()
        pass

    def testCollegeTracker(self):
        #Test all colleges in this test method
        pass"""


