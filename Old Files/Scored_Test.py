####################################################################################################################################################  
#  																																				   #
# This file has been generated by Amit Patankar:  																								   #
#     Created by              : amit.patankar																									   #	
#     Created on              : 11-07-2013																										   #
#     Directory               : /Desktop/																								           #
#     Purpose		    	  : This structure holds the attributes of each section in a text.							   						   #
#  													   																							   #
#################################################################################################################################################### #Test Class


#Scored Test Class
class Scored_Test(object):

	#This is the default constructor with all variables defined.
	def __init__(self, year, month, date):
		self.year = year
		self. month = month
		self.sections = {}


	def get_section(self, section_number):
		return self.sections[section_number]

	def add_section(self, section):
		self.sections[section.section_number] = section

	def get_ID(self):
		return "S" + FIELD_SEP + str(self.month) + FIELD_SEP + str(self.year) 