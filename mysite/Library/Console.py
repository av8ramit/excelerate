####################################################################################################################################################  
#                                                                                                                                                  #
# This file has been generated by Amit Patankar:                                                                                                   #
#     Created by              : amit.patankar                                                                                                      #    
#     Created on              : 11-08-2013                                                                                                         #
#     Directory               : /Desktop/                                                                                                          #
#     Purpose                 : This module allows for the console to input commands.                                                              #
#                                                                                                                                                  #
#################################################################################################################################################### 

from Commands import *
from Values import *
from License import *
from Class_Analytics import *
import subprocess

class Console(object):

    #This is the default constructor with all variables defined.
    def __init__(self):
        self.user = None
        self.state = LAUNCH_STATE
        self.error = None
        self.c = None  # c is class 

    def parse_command(self, user_input):
        if empty(user_input):
            return
        return user_input.split(SPACE)

    def process_commands(self, user_input):
        if (empty(user_input)):
            return True

        #date license check
        if not (check_date_license()):
            self.error = ("Error: This license of Excelerate has expired on " + date_of_expiration + ".")
            return False

        cmd_vector = self.parse_command(user_input)

        cmd = cmd_vector[COMMAND_INDEX] 
        
        #Clear Command
        if cmd == "clear":
            if (len(cmd_vector) == 2 and is_int(cmd_vector[1])):
                for i in range (0, int(cmd_vector[1])):
                    print (PROMPT)
                return True
            elif (len(cmd_vector) == 1):
                for i in range (0, 10):
                    print (PROMPT)
                return True
            else:
                self.error = ("Error: Invalid use of clear command.")
                return False

        #New Class
        if cmd == "new_class":
            if (len(cmd_vector) == 2 and not empty(cmd_vector[1])):
                if file_exists(class_directory(cmd_vector[1])):  #check to make sure class directory doesn't exist
                    self.error = ("Class record already exists. Please try again with a new name.")
                    return False
                else:
                    if (True):
                        self.c = new_class(cmd_vector[1])
                        self.state = CLASS_STATE
                        return True
                    else:
                        self.error = ("Error: You have exceeded the number of users purchased.")
                        return False
            else:
                self.error = ("Error: Invalid use of New Class command.")
                return False        


        #Load Class 
        if cmd == "load_class":        # command passed via GUI.py buttons
            if (len(cmd_vector) == 2 and not empty(cmd_vector[1])):  #check command length and contents
                if not file_exists(class_directory(cmd_vector[1])):   #check to make sure class directory exists
                    self.error = ("Class record does not exist. Please try again with a new name.")
                    return False
                else:
                    self.c = load_class(cmd_vector[1])
                    self.state = CLASS_STATE
                    return True
            else:
                self.error = ("Error: Invalid use of Load Class command.")
                return False          

        #New User
        if cmd == "new_student":
        
            if (self.state == CLASS_STATE or self.state == USER_STATE):   # make sure a class has been made or loaded
                
                if (len(cmd_vector) == 2 and not empty(cmd_vector[1])):
                    if file_exists(user_directory(cmd_vector[1], self.c.name)):
                        self.error = ("Student record already exists. Please try again with a new name.")
                        return False
                    else:
                        if (True):
                            self.user = new_user(cmd_vector[1], self.c.name)
                            self.c.add_student(cmd_vector[1])
                            self.state = USER_STATE
                            
                            return True
                        else:
                            self.error = ("Error: You have exceeded the number of users purchased.")
                            return False
                else:
                    self.error = ("Error: Invalid use of new student command.")
                    return False 
            else: 
                self.error = ("Error: Please create a new class or load an existing class before creating a new student")    
                return False 

        #Save Progress
        if cmd == "save":
            if (len(cmd_vector) == 1 and self.state == USER_STATE):
                self.user.save_user()
                return True
            else:
                self.error = ("Error: Invalid use of save command.")
                return False

        #Reset Account
        if cmd == "reset":
            if (len(cmd_vector) == 1 and self.state == USER_STATE):
                self.user.reset_account()
                return True
            else:
                self.error = ("Error: Invalid use of reset command.")
                return False

        #Load User
        if cmd == "load_student":
            if(self.state == CLASS_STATE or self.state == USER_STATE):
                if (len(cmd_vector) == 2 and not empty(cmd_vector[1])):
                    name = cmd_vector[1]
                    if (name in list_users(self.c.name)):
                        filename = user_filename(name, self.c.name)
                        if file_exists(filename):
                            self.user = load_user(name, filename, self.c.name)
                            self.state = USER_STATE
                            return True
                        else:
                            self.error = ("Error: No records found of given student " + name + ".")
                            return False
                    else:
                        self.error = ("Error: No records found of given student " + name + ".")
                        return False
                else:
                    self.error = ("Error: Invalid use of load student command.")
                    return False
            else: 
                self.error = ("Error: Please create a new class or load an existing class before creating a new student")    
                return False 
        #Delete User
        if cmd == "delete_student":
            if (len(cmd_vector) == 2 and not empty(cmd_vector[1])):
                name = cmd_vector[1]
                directory = user_directory(name)
                if (file_exists(directory)):
                    rmdir(directory)
                    self.state = LAUNCH_STATE
                    return True
                else:
                    self.error = ("Error: No records found of given student " + name + ".")
                    return False
            else:
                self.error = ("Error: Invalid use of delete student command.")
                return False

        #List Tests
        if cmd == "list_tests":
            if len(cmd_vector) == 1:
                list_tests()
                return True
            else:
                self.error = ("Error: Invalid use of list tests command.")
                return False

        #Print Answer Sheet
        if cmd == "answer_sheet":
            if self.state != USER_STATE:
                self.error = ("Error: Please load or create a user before creating answer sheets.")
                return False
            elif (len(cmd_vector) == 2 and not empty(cmd_vector[1])):
                if valid_test_id(cmd_vector[1]):
                    make_answer_sheet(self.user, cmd_vector[1])
                    return True
                else:
                    self.error = ("Error: Not a valid supported test_id.")
                    return False
            else:
                self.error = ("Error: Invalid use of answer sheet command.")
                return False

        #Grade
        if cmd == "grade":
            if self.state != USER_STATE:
                self.error = ("Error: Please load or create a user before grading tests.")
                return False            
            elif len(cmd_vector) == 2 and not empty(cmd_vector[1]):
                path =  user_directory(self.user.name , self.c.name) + DIR_SEP + cmd_vector[1]
                if file_exists(path):
                    try:
                        grade(self.user, path)
                        return True
                    except:
                        #CHANGE ERROR FUNCTION
                        self.error = ("Error: The answer sheet has been corrupted. Run the answer_sheet command and then input your answers in that file.")
                        return False
                else:
                    self.error = ("Error: Could not find " + cmd_vector[1] + " in " + self.user.name + " directory.")
                    return False
            else:
                self.error = ("Error: Invalid use of grade command.")
                return False

        #Print Simple Report
        if cmd == "simple_report":
            if self.state == LAUNCH_STATE:
                self.error = ("Error: Please load or create a user before grading tests.")
                return False
            elif self.user.tests_taken == []:
                self.error = ("Error: Please take tests and grade them before printing reports.")
                return False
            elif self.state == USER_STATE and self.user != None:
                 simple_report(self.user)
                 return True
            else:
                self.error = ("Error: Invalid use of grade command.")
                return False

        #Print Advanced Report
        if cmd == "advanced_report":
            if self.state == LAUNCH_STATE:
                self.error = ("Error: Please load or create a user before grading tests.")
                return False
            elif self.user.tests_taken == []:
                self.error = ("Error: Please take tests and grade them before printing reports.")
                return False
            elif self.state == USER_STATE and self.user != None:
                 advanced_report(self.user)
                 return True
            else:
                self.error = ("Error: Invalid use of grade command.")
                return False

        #Print Graph Report
        if cmd == "graph_report":
            if self.state == LAUNCH_STATE:
                self.error = ("Error: Please load or create a user before grading tests.")
                return False
            elif self.user.tests_taken == []:
                self.error = ("Error: Please take tests and grade them before printing reports.")
                return False
            elif self.state == USER_STATE and self.user != None:
                 graph_report(self.user)
                 return True
            else:
                self.error = ("Error: Invalid use of grade command.")
                return False

        #Print Section Reports
        if cmd == "section_report":
            if self.state == LAUNCH_STATE:
                self.error = ("Error: Please load or create a user before grading tests.")
                return False
            elif self.user.tests_taken == []:
                self.error = ("Error: Please take tests and grade them before printing reports.")
                return False
            elif self.state == USER_STATE and self.user != None:
                 section_report(self.user)
                 return True
            else:
                self.error = ("Error: Invalid use of grade command.")
                return False

        if cmd == "make_test":
            if self.state != LAUNCH_STATE:
                self.error = ("Error: You can only create tests at launch time.")
                return False
            else:
                make_test()
                return True

        if cmd == "class_analyze":
            if self.state == CLASS_STATE or self.state == USER_STATE:
                a = Analytics(self.c.name)      
                a.report()
                dirc = class_directory(self.c.name)
                os.system('open ' + dirc + DIR_SEP + 'analytics.html' )
                return True
            else:
                self.error = ("Error: Please load or create a class before running analysis on it.")
                return False



        #Help
        if cmd == "help":
            print ("")
            print ("Console Command Instructions:")
            print ("(optional field)")
            print ("[mandatory field]")
            print ("")
            print ('"clear (n)": Clears a line from the screen and if an input number of lines is given it clears the screen for n many lines.')
            print ("")
            print ('"new_student [name]": Creates a new account for a user with the specified name. ')
            print ("")
            print ('"load_student [name]": Loads the account for the user with the specified name.')
            print ("")
            print ('"delete_student [name]": Deletes the account for the user with the specified name.')
            print ("")
            print ('"save": Saves the tests that were taken in this session as the overall progress of the user.')
            print ("")
            print ('"reset": Resets the tests taken by a user and allows them to start over.')
            print ("")
            print ('"answer_sheet [test_id]": Creates an answer sheet based on a given test_id. Saves as csv file in the users directory and each section is correspondingly with the question number.')
            print ("")
            print ('"grade [filename]": Grades the given csv filename that was originally created by answer_sheet.')
            print ("")
            print ('"simple_report": Prints the basic report for a given user.')
            print ("")
            print ('"advance_report": Prints the advanced detailed report for a given user.')
            print ("")
            print ('"graph_report": Prints the graphs for each section.')
            print ("")
            print ('"section_report": Prints the advanced type report for each section.')
            print ("")

        #Invalid command        
        else:
            self.error = ("Error: Command " + cmd + " not recognized.")
            return False




