def compare_list(list1,list2):
	if list1 == list2:
		print "the lists are the same"
	else:
		print "the lists are not the same"


list_one = [1,2,5,6,3]
list_two = [1,2,5,6,2]

compare_list(list_one,list_two)

#First attempt

# def compare_list(list1,list2):
# 	length1 = len(list1)
# 	length2 = len(list2)
# 	if length1 == length2:
# 		print "The lists are the same length."
# 		for i in range(length1):
# 			temp = list1[i]
# 			for v in range(length2):
# 				v = i
# 				temp2 = list2[v]
# 				if temp2 != temp:
# 					print "The lists are not the same"
# 					break
# 				else:
# 					print "The value of list 1 at", i, "and the value of list 2 at", v, "are the same."
# 					break
# 	else:
# 		print "The lists are not the same."


# list_one = [1,2,5,6,3]
# list_two = [1,2,5,6,2]