import re

def check_leap(y):
	year = int(y)
	if (year % 4) == 0:
		if (year % 100) == 0:
			if (year % 400) == 0:
				return year
		else:
			return year

def check_month(m, y):
	month = int(m)
	if 1 <= month <= 12:
		if month in [4, 6, 9, 11]:
			days = 30 	
		elif month == 2:
			if check_leap(y):
				days = 29
			else:
				days = 28
		else:
			days = 31
	return days

def check_date(d, m, y):
	day = int(d)
	if day <= check_month(m, y):
		return d 	

date = "29-02-1200"
r = re.compile("^(?P<day>[0-9]{2})-(?P<month>[0-9]{2})-(?P<year>[0-9]{4})$")
s = re.search(r, date)
if s and check_date(s.group('day'), s.group('month'), s.group('year')):
		print(date)	
else:
	print("Invalid date")



email = "12ab.cd_12@xyz.tech.in"
r = re.compile("^[a-z0-9]+(\.[a-z0-9]+)?(_[a-z0-9]+)?@[a-z0-9]+(\.[a-z]{2,4}){1,2}$")
s = re.search(r, email)
if s:
	print(email)
else:
	print("Invalid mail")



text = "The code is available at www.edyoda.com/code/python and www.github.com/edyoda/python"
r = re.compile("www\.[a-z]+\.com/[a-z]+/[a-z]+")
s = re.findall(r, text)

for i in s:
	text = text.replace(i, '<a href="{}">{}</a>'.format(i, i.split('.')[1].capitalize()))

print(text)

