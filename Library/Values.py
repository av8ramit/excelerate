import os
import shutil
import random

#Question Value
PARSED_ARRAY_SIZE = 5

NUMBER_INDEX = 0
ANSWER_INDEX = 1
DIFFICULTY_INDEX = 2
RANGE_INDEX = 3
TYPE_INDEX = 4

#Section Value
ESSAY_SECTION_INDEX = 1
LABEL_VECTOR = ['Number', 'Answer', 'Difficulty', 'Range', 'Type']
READING_TYPE = 0
WRITING_TYPE = 1
MATH_TYPE = 2
ESSAY_TYPE = 3
TRIAL_TYPE = 4
SECTION_COUNT = 10
READING_SIZE = 67
MATH_SIZE = 54
WRITING_SIZE = 49

#Grading Value
GRADED_ARRAY_SIZE = 5
SECTION_ID_INDEX = 0
CA_INDEX = 1
IA_INDEX = 2
DIFF_INDEX = 3
QTYPE_INDEX = 4

#ID Value
FIELD_SEP = '_'

#Report Value
SECTION_SEP = "----------------------------------------------------------------------------------------------------"

#File Extensions
CSV = ".csv"
TXT = ".txt"

endl = "\n"

#Directory Values
DIR_SEP = "/"
PAR_DIR = ".."

#File Value
KEY_VECTOR = ['Section:', 'Type:', 'Size:']
KEYFILE = "key.csv"
SCOREFILE = "score.csv"
KEY_TYPE = 1
KEY_SIZE = 2
ANSWER_VECTOR = ['Number:', 'Answer:']
SCORE_VECTOR = ['Raw Score:', 'Writing', 'Math', 'Reading']

#CHARACTER VALUES
SPACE = ' '

#CONSOLE VALUES
COMMAND_INDEX = 0
LAUNCH_STATE = 0
LOAD_STATE = 1
PROMPT = ">>> "


TYPE_ARRAY = [WRITING_TYPE, MATH_TYPE, READING_TYPE]


#QUESTION TYPE VALUES

#WRITING
WRITING_TYPES = 5
WRITING_TYPE_1 = "W1"
WRITING_TYPE_2 = "W2"
WRITING_TYPE_3 = "W3"
WRITING_TYPE_4 = "W4"
WRITING_TYPE_5 = "W5"

WRITING_TYPE_DICT = {}
WRITING_TYPE_DICT[WRITING_TYPE_1] = "Verb Tense Agreement"
WRITING_TYPE_DICT[WRITING_TYPE_2] = "Prepositional Phrases"
WRITING_TYPE_DICT[WRITING_TYPE_3] = "Noun Pronoun Agreement"
WRITING_TYPE_DICT[WRITING_TYPE_4] = "Punctuation and Purpose"
WRITING_TYPE_DICT[WRITING_TYPE_5] = "Correct Sentences"


#MATH
MATH_TYPES = 6
MATH_TYPE_1 = "M1"
MATH_TYPE_2 = "M2"
MATH_TYPE_3 = "M3"
MATH_TYPE_4 = "M4"
MATH_TYPE_5 = "M5"
MATH_TYPE_6 = "M6"

MATH_TYPE_DICT = {}
MATH_TYPE_DICT[MATH_TYPE_1] = "Geometry (Triangles and Circles)"
MATH_TYPE_DICT[MATH_TYPE_2] = "Trigonometry and Angles"
MATH_TYPE_DICT[MATH_TYPE_3] = "Probability and Statistics"
MATH_TYPE_DICT[MATH_TYPE_4] = "Algebra"
MATH_TYPE_DICT[MATH_TYPE_5] = "Arithmetic"
MATH_TYPE_DICT[MATH_TYPE_6] = "Numbers and Operations"


#READING
READING_TYPES = 4
READING_TYPE_1 = "R1"
READING_TYPE_2 = "R2"
READING_TYPE_3 = "R3"
READING_TYPE_4 = "R4"

READING_TYPE_DICT = {}
READING_TYPE_DICT[READING_TYPE_1] = "Vocabulary"
READING_TYPE_DICT[READING_TYPE_2] = "Reasoning and Deduction"
READING_TYPE_DICT[READING_TYPE_3] = "Literal Comprehension"
READING_TYPE_DICT[READING_TYPE_4] = "Passage Comparison"


#Advice

#Colors
RED = "red"
YELLOW = "blue"
GREEN = "00CC00"

#positive
pa1 = "Good Job!"
pa2 = "Fantastic! Well done."
pa3 = "You are performing well."
pa4 = "Great work."
pa5 = "You've been improving a lot."
positive = [pa1, pa2, pa3, pa4, pa5]
p_thresh = 0.7

#average
aa1 = "Your performance here is okay. Focus on other weaker areas first."
aa2 = "Your scores in this category are average."
aa3 = "Improve in these areas once you have finished working on your more poor areas."
average = [aa1, aa2, aa3]
a_thresh = 0.4

#negative
na1 = "Uh oh, you need some work in this category."
na2 = "Unfortunately, you are not as strong in this area."
na3 = "You need some improvement here."
na4 = "Here is a great place to improve and score higher."
na5 = "Try focussing more in this area to increase your score."
negative = [na1, na2, na3, na4, na5]

#guessing
ga1 = "Your guesses in this category are often wrong. Consider leaving them blank."
ga2 = "Leave more questions in these catgories blank. You are losing 1/4th a point for each one you miss."
ga3 = "Instead of guessing, leave these questions blank."
ga4 = "Guessing in this category is a much better option and will improve your score."
guess = [ga1, ga2, ga3, ga4]

def div(x, y):
  return float(x) / float(y)

def random_choice(array):
  return array[(int(random.random() * 100) % len(array))]

def get_section_type_size(section_type):
  if section_type == WRITING_TYPE:
    return ("W", WRITING_TYPES)
  elif section_type == MATH_TYPE:
    return ("M", MATH_TYPES)
  elif section_type == READING_TYPE:
    return ("R", READING_TYPES)
  else:
    print ("Error: You are looking for data to an invalid section.")
    return None

#LEVEL TYPES
LEVEL_1 = "L1"
LEVEL_2 = "L2"
LEVEL_3 = "L3"
LEVEL_4 = "L4"
LEVEL_5 = "L5"

"""def round_dec(f, n):
  if isinstance(f, int):
    return f
  f = f * pow(10,n)
  f = f - f%1
  f = f / pow(10,n)
  return f"""

def percentage(decimal):
  decimal *= 100
  output = str(int(decimal)) + "%"
  return output

average_bound1 = 500
average_bound2 = 600

def qualitative_color(score):
  if score < average_bound1:
    return RED
  elif score > average_bound2:
    return GREEN
  else:
    return YELLOW

def qualitative(score):
  if score < average_bound1:
    return "Poor"
  elif score > average_bound2:
    return "Proficient"
  else:
    return "Average"

def overall_qualitative_color(score):
  return qualitative_color(score / 3)

def overall_qualitative(score):
  return qualitative(score / 3)


#round the questions missed deduction down
def round_rem(dec):
  if dec % 1 > 0.5:
    return 1
  return 0

def random_number(n):
  return int(random.random() * 100) % n

def string_to_array(data):
  data = data[1:-1]
  array = []
  data = data.replace(' ', "")
  data = data.replace('(', "")
  data = data.replace(')', "")
  data = data.replace("'", "")
  data = data.split(',')
  i = 0
  for entry in data:
    if i % 2 == 0:
      q_id = entry
    if i % 2 == 1:
      array.append((q_id, entry))
    i+=1
  return array

def is_int(s):
    try:
        int(s)
        return True
    except ValueError:
        return False

def empty(s):
  if isinstance(s, list):
    return s == []
  if isinstance(s, str):
    return s == ""

def file_exists(filename):
  return os.path.exists(filename)

def user_directory(name):
  return "Users" + DIR_SEP + name 

def user_filename(name):
  return "Users" + DIR_SEP + name + DIR_SEP + name + TXT

def valid_test_id(test_id):
  if file_exists(test_id):
    array = test_id.split('_')
    if len(array) == 2:
      if is_int(array[0]) and is_int(array[1]):
        return True
  return False

def mkdir(dir_name):
  os.mkdir(dir_name)

def rmdir(dir_name):
  shutil.rmtree(dir_name)

def parse_missed(array):
  blank = 0
  incorrect = 0
  for question in array:
    if question[1] == '?':
      blank += 1
    else:
      incorrect+=1
  return (blank, incorrect)

def is_null(n):
  return n == None

def section_size(section_type):
  if section_type == MATH_TYPE:
    return MATH_SIZE
  elif section_type == WRITING_TYPE:
    return WRITING_SIZE
  elif section_type == READING_TYPE:
    return READING_SIZE
  else:
    print ("Error invalid section type.")
    return 0

def section_name(section_type):
  if section_type == MATH_TYPE:
    return "Math"
  elif section_type == WRITING_TYPE:
    return "Writing"
  elif section_type == READING_TYPE:
    return "Reading"
  else:
    print ("Error invalid section type.")
    return 0

def index_exists(dictionary, key):
  return key in dictionary.keys()

