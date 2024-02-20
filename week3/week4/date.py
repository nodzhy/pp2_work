#task 1
"""
import datetime
today=datetime.datetime.now()
five_day=today-datetime.timedelta(days=5)
print(five_day)
"""
#task 2
"""
import datetime
today=datetime.datetime.now()
yest=today-datetime.timedelta(days=1) 
tom=today+datetime.timedelta(days=1)
print("today: ", today)
print("----------------")
print("Yesterday: ", yest) 
print("----------------")
print("tommorow: ", tom)
"""
#task 3
"""
import datetime
today=datetime.datetime.now()
print(today.strftime("%d-%m-%Y, %H-%M-%S"))
"""
#task 4
"""
import datetime
today=datetime.datetime.now() 
print("напиши через сколько дней")
day_first=input() 
print("напиши через сколько дней")
day_second=input()
first=today+datetime.timedelta(days=int(day_first))
second=today+datetime.timedelta(days=int(day_second))
dif=second-first
print(dif)
"""