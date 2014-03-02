# Testing suite for Analyze.py

from Value import *
from Key import *
from Scored import *
from Summary import *
from Data import *
from Graph import *
import csv

class TestsAnalyze(object):

	if __name__ == '__main__':
		debug = readCommand(sys.argv)   # True if we want to have debugging output printed out
		runTests(debug)

	def readCommand(args):
		if (args[0].equals('--debug'):
			return True
		else:
			return False

	def runTests(debug):

		analyzeTest = Analyze()
		analyzeTest.setDebug(debug)

		print "Running Analyze Tests\n\n"
		
		print "Running Data Import Check\n"

	def buildTestUser():
		testUser = User("analyzeTestUser")
		recreate_user(User.directory)
		