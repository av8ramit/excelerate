####################################################################################################################################################  
#                                                                                                                                                  #
# This file has been generated by Kevin Koh:                                                                                                       #
#     Created by              : Kevin Koh                                                                                                          #    
#     Created on              : 15-02-2014                                                                                                         #
#     Directory               : /Library/                                                                                                          #
#     Purpose                 : This file will perform analysis on user test scores                                                                #
#                                                                                                                                                  #
####################################################################################################################################################

from Values import *
from Key import *
from Scored import *
from Summary import *
from Data import *
from Graph import *
from scipy import stats
import math
import csv

#Main analytics runner
class Analyze(object):

	#This is the default constructor
	def __init__(self):
		self.dataSet = [] # List of data values
		self.debug = False

	def setDebug(self, status):
		self.debug = status

	def printDebug(self, statement):
		if self.debug:
			print (statement)

	def importData(self, data):
		self.dataSet.append(data)

	def linearRegression(self):
		for qType in TYPE_ARRAY:
			dataDict = 

	def linearRegression(self, section):
		resultList = []
		dataSet = self.getSectionInfo(qType, "Correct")


	# Finds Standard Deviation of a set based on miss or correct and then plots it to the mean
	def plotConsistencyGraph(self, qStat):
		resultList = []		
		for qType in TYPE_ARRAY:
			dataDict = self.getSectionInfo(qType, qStat)
			localMean = self.calculateMean(dataDict)
			localSD = self.calculateSD(dataDict)
			resultList.append(qType, localMean, localSD)
		return resultList

	def plotConsistencyByType(self, qType, qStat):
		resultList = []
		dataSoFar = []
		dataDict = self.getSectionInfo(qType, qStat)
		for dataPointKey in dataDict.keys():
			dataPoint = dataDict[dataPointKey]
			dataSoFar.append(dataPoint)
			sd = self.calculateSD(dataSoFar)
			resultList.append( (dataPoint, sd) )
		return resultList

	def getSectionInfo(self, type):

		if type == WRITING_TYPE:
			size = WRITING_TYPES
			tag = "W"
		elif type == MATH_TYPE:
			size == MATH_TYPES
			tag = "M"
		elif type == READING_TYPE:
			size == READING_TYPES
			tag = "R"

		outputSet = []

		for data in dataSet:
			for i in range(1, size + 1):
				fulltag = tag + str(i)
				testID = ""
				printDebug("Looking in " + fulltag)
				qStats = data[type].stats[fulltag]
				dataPiece = DataContainer(fulltag, testID, qStats.c, qStats.m, qStats.b, qStats.t)
				outputSet.append(dataPiece)

		return outputSet

	def scoreCalculate(correct, miss, total):
		score = correct - miss/4
		# This may have to be more extensively customized based upon subject test,
		# section specific scoring, etc.


class DataContainer(object):

	def __init__(self, tag, context, correct, miss, blank, total):
		self.tag = tag
		self.context = context
		self.correct = correct
		self.miss = miss
		self.blank = blank
		self.total = total

	def getCorrectPercentage():
		return self.correct/self.total

	def getTotal():
		return self.total

	def getCorrect():
		return self.correct

	def getContext():
		return self.context








		