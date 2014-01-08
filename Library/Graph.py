####################################################################################################################################################  
#  																																				   #
# This file has been generated by Amit Patankar:  																								   #
#     Created by              : amit.patankar																									   #	
#     Created on              : 08-08-2013																										   #
#     Directory               : /Desktop/																								           #
#     Purpose		    	  : This file represents a data graph.														   						   #
#  													   																							   #
#################################################################################################################################################### 

from Values import *

class Graph(object):

	def __init__(self, points):
		self.g = ""
		for y in range(0,20):
			for x in range(0,20):
				if x == 0:
					self.g += "\t|"
				elif x == 19:
					self.g += "\n"
				else:
					self.g += "  "
		self.g += "\t|"
		for i in range(0,36):
			self.g += "_"
		self.g += endl

	def __str__(self):
		return self.g

a = Graph(20)
print(a)