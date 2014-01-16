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
import subprocess

class Console(object):

    #This is the default constructor with all variables defined.
    def __init__(self):
        self.user = None
        self.state = LAUNCH_STATE

    def parse_command(self, user_input):
        if empty(user_input):
            return
        return user_input.split(SPACE)

    def process_commands(self, user_input):
        if (empty(user_input)):
            return True
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
                print ("Error: Invalid use of clear command.")
                return False

        #New User
        if cmd == "new_user":
            if (len(cmd_vector) == 2 and not empty(cmd_vector[1])):
                if file_exists(user_directory(cmd_vector[1])):
                    print ("User record already exists. Please try again with a new name.")
                else:
                    self.user = new_user(cmd_vector[1])
                    self.state = LOAD_STATE
                return True
            else:
                print ("Error: Invalid use of new_user command.")
                return False

        #Save Progress
        if cmd == "save":
            if (len(cmd_vector) == 1 and self.state == LOAD_STATE):
                self.user.save_user()
                return True
            else:
                print ("Error: Invalid use of save command.")
                return False

        #Reset Account
        if cmd == "reset":
            if (len(cmd_vector) == 1 and self.state == LOAD_STATE):
                self.user.reset_account()
                return True
            else:
                print ("Error: Invalid use of reset command.")
                return False

        #Load User
        if cmd == "load_user":
            if (len(cmd_vector) == 2 and not empty(cmd_vector[1])):
                name = cmd_vector[1]
                filename = user_filename(name)
                if (file_exists(filename)):
                    self.user = load_user(name, filename)
                    self.state = LOAD_STATE
                    return True
                else:
                    print ("Error: No records found of given user.")
                    return False
            else:
                print ("Error: Invalid use of load_user command.")
                return False

        #Load User
        if cmd == "list_tests":
            if len(cmd_vector) == 1:
                list_tests()
                return True
            else:
                print ("Error: Invalid use of list_tests command.")
                return False


        #Print Answer Sheet
        if cmd == "answer_sheet":
            if self.state != LOAD_STATE:
                print ("Error: Please load or create a user before creating answer sheets.")
                return False
            elif (len(cmd_vector) == 2 and not empty(cmd_vector[1])):
                if valid_test_id(cmd_vector[1]):
                    make_answer_sheet(self.user, cmd_vector[1])
                    return True
                else:
                    print ("Error: Not a valid supported test_id.")
                    return False
            else:
                print ("Error: Invalid use of answer_sheet command.")
                return False

        #Grade
        if cmd == "grade":
            if self.state != LOAD_STATE:
                print ("Error: Please load or create a user before grading tests.")
                return False            
            elif len(cmd_vector) == 2 and not empty(cmd_vector[1]):
                path = self.user.directory() + DIR_SEP + cmd_vector[1]
                if file_exists(path):
                    try:
                        grade(self.user, path)
                        return True
                    except:
                        print("Error: The answer sheet has been corrupted. Run the answer_sheet command and then input your answers in that file.")
                        return False
                else:
                    print ("Error: Could not find " + cmd_vector[1] + " in " + self.user.name + " directory.")
                    return False
            else:
                print ("Error: Invalid use of grade command.")
                return False

        #Print Simple Report
        if cmd == "simple_report":
            if self.state == LAUNCH_STATE:
                print ("Error: Please load or create a user before grading tests.")
                return False
            elif self.user.tests_taken == []:
                print ("Error: Please take tests and grade them before printing reports.")
                return False
            elif self.state == LOAD_STATE and self.user != None:
                 simple_report(self.user)
                 return True
            else:
                print ("Error: Invalid use of grade command.")
                return False

        #Print Advanced Report
        if cmd == "advanced_report":
            if self.state == LAUNCH_STATE:
                print ("Error: Please load or create a user before grading tests.")
                return False
            elif self.user.tests_taken == []:
                print ("Error: Please take tests and grade them before printing reports.")
                return False
            elif self.state == LOAD_STATE and self.user != None:
                 advanced_report(self.user)
                 return True
            else:
                print ("Error: Invalid use of grade command.")
                return False

        #Print Graph Report
        if cmd == "graph_report":
            if self.state == LAUNCH_STATE:
                print ("Error: Please load or create a user before grading tests.")
                return False
            elif self.user.tests_taken == []:
                print ("Error: Please take tests and grade them before printing reports.")
                return False
            elif self.state == LOAD_STATE and self.user != None:
                 graph_report(self.user)
                 return True
            else:
                print ("Error: Invalid use of grade command.")
                return False

        #Print Section Reports
        if cmd == "section_report":
            if self.state == LAUNCH_STATE:
                print ("Error: Please load or create a user before grading tests.")
                return False
            elif self.user.tests_taken == []:
                print ("Error: Please take tests and grade them before printing reports.")
                return False
            elif self.state == LOAD_STATE and self.user != None:
                 section_report(self.user)
                 return True
            else:
                print ("Error: Invalid use of grade command.")
                return False

        if cmd == "make_test":
            if self.state != LAUNCH_STATE:
                print ("Error: You can only create tests at launch time.")
                return False
            else:
                make_test()
                return True


        #Help
        if cmd == "help":
            print ("")
            print ("Console Command Instructions:")
            print ("(optional field)")
            print ("[mandatory field]")
            print ("")
            print ('"clear (n)": Clears a line from the screen and if an input number of lines is given it clears the screen for n many lines.')
            print ("")
            print ('"new_user [name]": Creates a new account for a user with the specified name. ')
            print ("")
            print ('"load_user [name]": Loads the account for the user with the specified name.')
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
            print ("Error: Command " + cmd + " not recognized.")
            return False




