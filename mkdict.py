def mkdict(list1,list2):
	newlist = zip(list1,list2)
	new_dict = dict(newlist)
	print new_dict


name = ["Anna", "Eli", "Pariece", "Brendan", "Amy", "Shane", "Oscar"]
favorite_animal = ["horse", "cat", "spider", "giraffe", "ticks", "dolphins", "llamas"]

mkdict(name,favorite_animal)