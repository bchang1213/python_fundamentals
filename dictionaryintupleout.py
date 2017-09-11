def dicttupe(dict):
	arr = []
	tupla = ()
	for key,value in dict.iteritems():
		tupla = (key,value)
		arr.append(tupla)
	print arr





# function input
my_dict = {
  "Speros": "(555) 555-5555",
  "Michael": "(999) 999-9999",
  "Jay": "(777) 777-7777"
}

dicttupe(my_dict)
#function output
# [("Speros", "(555) 555-5555"), ("Michael", "(999) 999-9999"), ("Jay", "(777) 777-7777")]
