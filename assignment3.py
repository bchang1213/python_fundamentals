def findtype(val):
	#Is it a string?
	if isinstance(val,str) and len(val) >= 50:
		print "Long sentence."
	if isinstance(val,str) and len(val) < 50:
		print "Short sentence."
	#Is it an integer?
	if isinstance(val,int) and val >= 100:
		print "That's a big number!"
	if isinstance(val,int) and val < 100:
		print "That's a small number."
	#Is it a list?
	if isinstance(val,list) and len(val) >= 10:
		print "Big list!"
	if isinstance(val,list) and len(val) < 10:
		print "Short list!"
