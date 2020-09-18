def weekday(n):
	day={0:'monday',
	    1:'tuesday',
	    2:'wednesday',
	    3:'thursday',
	    4:'friday',
	    5:'saturday',
	    6:'sunday'
	}
	return day[n]

t = int(input(''))
i=0
while i<t:
	i = i + 1
	n = int(input(''))
	print (weekday(n))
