def find_char(list,char):
	new_list = []
	length1 = len(list)
	for value in range(0,length1):
		val1 = list[value]
		for letters in range(0,len(val1)):
			if val1[letters] == char:
				new_list.append(val1)
				break
	print new_list

word_list = ['hello','world','my','name','is','Anna']
char1 = 'o'

find_char(word_list,char1)