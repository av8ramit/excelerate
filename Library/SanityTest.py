from Values import *
from Key import *
from Scored import *
from Summary import *
from Data import *
from Graph import *
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
		name = "dummy"
		res = c.process_commands('new_student ' + name)
        if (not res):
            raise SetupTeardownError("Failed to set up.")
        else:     
            var = StringVar()
            if(c.state == LOAD_STATE):
                UserName = c.user.name
                var.set(UserName)

	def tearDown(self):
		# delete a test user here along with all data related to it
		name = "dummy"
		res = c.process_commands('delete_student ' + name)
		if (not res):
			raise SetupTeardownError("Failed to tear down. Manually reset the environment before testing.")


	def testLoadUser(self):
		#Test the loading of a user

	def testImportData(self):
		#test importing test data

	def testCreateTest(self):
		 #Create a dummy test

	def testCreateAnswerSheet(self):
		#Create an answer sheet to the dummy test created above

	def testAutoGrader(self):
		#Autograde the dummy test with the test user's data

	def testSaveChanges(self):
		#Check the functionality of this

	def testSimpleReport(self):
		#Test the data sent to the html creator. Don't actually launch any reports

	def testAdvancedReport(self):
		#Same as above

	def testSectionReport(self):
		#Same as above

	def testGraphsReport(self):
		#Same as above

	def testClassAnalytics(self):
		#Test the functionality of class analytics. Should be isolated from other users, and class should only include the test user. Or we can run classAnalytics, but only have the assertion statement check for the test user we created in setup()

	def testCollegeTracker(self):
		#Test all colleges in this test method


