####################################################################################################################################################  
#  																																				   #
# This file has been generated by Amit Patankar:  																								   #
#     Created by              : amit.patankar																									   #	
#     Created on              : 14-07-2013																										   #
#     Directory               : /Desktop/																								           #
#     Purpose		    	  : This structure holds the data stored indexed by type or difficulty.						   						   #
#  													   																							   #
####################################################################################################################################################

from Values import *

class Data_Holder(object):

	#This is the default constructor takes an id and stores analysis reports.
	def __init__(self):
		self.data = {}
		self.data[WRITING_TYPE] = Section_Data_Holder(WRITING_TYPE)
		self.data[MATH_TYPE] = Section_Data_Holder(MATH_TYPE)
		self.data[READING_TYPE] = Section_Data_Holder(READING_TYPE)

	def __str__(self):
		output = ""
		for key in self.data.keys():
			output += section_name(key)
			output += endl
			output += str(self.data[key])
			output += endl
		return output


class Section_Data_Holder(object):

	#This is the default constructor takes an id and stores analysis reports.
	def __init__(self, section_type):	
		self.stats = {}
		self.type = section_type
		tple = get_section_type_size(self.type)
		#for i in range(0,tple[1]):
		#	self.stats[tple[0] + str(i)] = Question_Stats()
		for i in range(1,6):
			self.stats["L" + str(i)] = Question_Stats()

		if self.type == WRITING_TYPE:
			for i in range(1, WRITING_TYPES + 1):
				self.stats["W" + str(i)] = Question_Stats()

		if self.type == READING_TYPE:
			for i in range(1, READING_TYPES + 1):
				self.stats["R" + str(i)] = Question_Stats()

		if self.type == MATH_TYPE:
			for i in range(1, MATH_TYPES + 1):
				self.stats["M" + str(i)] = Question_Stats()


	def __str__(self):
		output = ""
		for key in self.stats.keys():
			output += (key + SPACE + str(self.stats[key]))
		return output


class Question_Stats(object):

	#This is the default constructor takes an id and stores analysis reports.
	def __init__(self):
		self.t = 0
		self.c = 0
		self.m = 0
		self.b = 0

	def add_correct(self):
		self.c += 1
		self.t += 1

	def add_miss(self):
		self.m += 1
		self.t += 1

	def add_blank(self):
		self.b += 1
		self.t += 1

	#def advice(self):

		

	def __str__(self):
		output = ""
		output += "T: "
		output += str(self.t)
		output += " | "
		output += "C: "
		output += str(self.c)
		output += " | "
		output += "M: "
		output += str(self.m)
		output += " | "
		output += "B: "
		output += str(self.b)
		output += endl
		return output
