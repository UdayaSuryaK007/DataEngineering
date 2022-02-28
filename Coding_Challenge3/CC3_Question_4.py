#Write a Python program to print the dates of yesterday, today, and tomorrow.
from datetime import date, timedelta
print('Yesterday : '+str(date.today()-timedelta(1)))
print('Today: '+str(date.today()))
print('Tomorrow: '+str(date.today()+timedelta(1)))