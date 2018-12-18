import calendar
a,b,c=map(int,input().split())
day_number = calendar.weekday(c, a, b)
day_name = calendar.day_name[day_number]
print(day_name.upper())