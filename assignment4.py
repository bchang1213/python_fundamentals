def listtype(umlist):
	length = len(umlist)
	string = ""
	thesum = 0
	if isinstance(umlist,list):
		for value in range(umlist):
			if isinstance(value,str):
				string += value
			if isinstance(umlist[i], int):
				thesum += value

	if string and thesum:
		print "The array you entered is of mixed type"
		print "String:",string
		print "Numbers total:" the sum

	elif string:
		print "The array you entered is of string type."
		print "String:",string

	else:
		print "The array you entered is of number (int or float) type."
		print thesum