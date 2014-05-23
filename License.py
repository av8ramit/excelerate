from Values import *
import datetime



def check_date_license():
	DATE_LICENSE_VALID = True
	todays_date_array = str(datetime.date.today()).split('-')
	expire_date_array = EXPIRATION_DATE.split('/')

	year = 0
	month = 1
	day = 2

	#Year Check
	if int(todays_date_array[year]) > int(expire_date_array[year]):
		DATE_LICENSE_VALID = False
	elif int(todays_date_array[year]) < int(expire_date_array[year]):
		DATE_LICENSE_VALID = True
	else:
		#Month Check
		if int(todays_date_array[month]) > int(expire_date_array[month]):
			DATE_LICENSE_VALID = False
		elif int(todays_date_array[month]) < int(expire_date_array[month]):
			DATE_LICENSE_VALID = True
		else:
			#Day Check
			if int(todays_date_array[day]) > int(expire_date_array[day]):
				DATE_LICENSE_VALID = False
			elif int(todays_date_array[day]) < int(expire_date_array[day]):
				DATE_LICENSE_VALID = True
			else:
				DATE_LICENSE_VALID = False
	return DATE_LICENSE_VALID


def user_limit_license():
	USER_LICENSE_VALID = True
	a = os.listdir(user_directory(''))
	total_users = 0
	for directory in a:
		if file_exists(user_directory(directory) + DIR_SEP + directory + TXT):
			total_users += 1
	if (total_users >= USER_LIMIT):
		USER_LICENSE_VALID = False
	return USER_LICENSE_VALID

