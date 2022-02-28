#Print today's date in the format given below.
#Day_name Day_number Month_name Year
from datetime import date
date_var = date.today()
print("Today's date is: "+ str(date_var.strftime('%A %d %B %Y')))