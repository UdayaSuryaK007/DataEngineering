from datetime import datetime, timedelta, date, timedelta
#Expected Output:
#Current date and time: 2020-10-17 16:02:50.583157
print('Q1-output:'+ '\n' + str(datetime.now())+ '\n')

#Q2: Print the month and minutes from the datetime object given below.
dob_time = datetime(1995, 6, 14, 10, 37, 50, 0)
print('Q2-output:'+ '\n' + "Month: " + dob_time.strftime("%m")+ '\n' + "Minutes: " + dob_time.strftime("%M") + '\n')

#Q3: Print the date in the format given below.
#Day_number Month_name(abbr.) Year - Day_name(abbr.)
given_date = datetime(2011, 10, 12)
print('Q3-output:'+ '\n' + given_date.strftime("%d %b %Y - %a")+ '\n')

#Q4: Write a Python program to find the day of the week of a given date?
given_date = datetime(2008, 5, 15)
print('Q4-output:'+ '\n' + given_date.strftime("%A")+ '\n')

#Q5: Write a Python program to add 2 days and 10 hours to a given date.
given_date = datetime(2016, 2, 27, 11, 30, 0)

final_datetime = given_date + timedelta(days=2, hours=10)
print('Q5-output:'+ '\n' + str(final_datetime)+ '\n')

#Q6: Write a Python program to calculate the number of days between two given dates.
date_1 = datetime(2020, 7, 21).date()
date_2 = datetime(2020, 3, 10).date()
print('Q6-output:'+ '\n' + str((date_1 - date_2).days)+ '\n')

#Q7: Write a Python program to convert a string to datetime.
myString = 'Oct 12 2002 12:45 PM'
datetime_obj = datetime.strptime(myString, '%b %d %Y %I:%M %p')
print('Q7-output:'+ '\n' + str(datetime_obj)+ '\n')
#print(type(datetime_obj))

#Q8: Print the date, day name, and time in the format given below.
# Day_number-Month_number-Year - Day_name - Hours:Minutes:Seconds
dob_time = datetime(1995, 6, 14, 10, 37, 50, 0)
print('Q8-output:'+ '\n' + dob_time.strftime('%d-%m-%Y-%a-%H:%M:%S')+ '\n')

#Q9: Write a Python program to print yesterdays' date.
today_date = date.today()
# print(today_date)
yesterday_date = today_date-timedelta(days=1)
print('Q9-output:'+ '\n' + str(yesterday_date)+ '\n')

#Q10: Write a Python program to print the next 5 days from the date given below.
given_date = datetime(2020, 10, 17)
days = 5
print('Q10-output:')
for i in range(1,days+1):
    print(given_date+timedelta(days = i))