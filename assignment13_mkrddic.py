# def names(seq):
# 	for i in seq:
# 		print i['first_name'],i['last_name']

# students = [
#      {'first_name':  'Michael', 'last_name' : 'Jordan'},
#      {'first_name' : 'John', 'last_name' : 'Rosales'},
#      {'first_name' : 'Mark', 'last_name' : 'Guillen'},
#      {'first_name' : 'KB', 'last_name' : 'Tonel'}
# ]
# names(students)



def morenames(seq):
	for titles in users:
		print titles
		number = 0
		for dictionary in users[titles]:
			count = 0
			number += 1
			print number,
			for letters in dictionary['first_name']:
				count += 1
			print "-",dictionary['first_name'],
			for dletters in dictionary['last_name']:
				count += 1
			print dictionary['last_name'],
			print "=",count


users = {
 'Students': [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
  ],
 'Instructors': [
     {'first_name' : 'Michael', 'last_name' : 'Choi'},
     {'first_name' : 'Martin', 'last_name' : 'Puryear'}
  ]
 }

morenames(users)