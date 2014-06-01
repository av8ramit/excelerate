from Values import *
from Key import *
from Scored import *
from Summary import *
from Data import *
from Graph import *
import csv
import unittest

class SanityTest(unittest.TestCase):

	def setUp(self):
		# construct a test user here

	def tearDown(self):
		# delete a test user here along with all data related to it

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


