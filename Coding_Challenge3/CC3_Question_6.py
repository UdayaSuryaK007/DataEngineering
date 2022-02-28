#We have the time in seconds given below. Convert this time into days, hours, minutes, and seconds.
from datetime import date, datetime, timedelta
time = 996452
day = time//86400  # 60(min) * 60(sec) * 24(hurs) -- 86400 Sec's/day
hour = (time-day*86400)//(3600)  # 60(min) * 60(sec) -- 3600 Sec's/hour 
minute = (time-day*86400 - hour*3600)//60  # 60 sec/minute
second = time- day*86400 - hour*3600 - minute*60
print("Days : Hours : Minutes : Seconds ->",'{} : {} : {} : {}'.format(day, hour, minute, second))