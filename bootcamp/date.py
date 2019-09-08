import datetime

now = datetime.datetime.now()

print(now)
print(now.year)
print(now.month)
print(now.day)
print(now.hour)
print(now.minute)
print(now.second)
print(now.microsecond)

print(now.weekday())

print(now + datetime.timedelta(weeks=1))

