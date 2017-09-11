def score_grades():
	print "Scores and Grades"
	for i in range(10):
		import random
		random_num = random.randint(60,100)
		if 60 < random_num <= 69:
			print "Score:",random_num,"; Your grade is D"
		elif 70 < random_num <= 79:
			print "Score:",random_num,"; Your grade is C"
		elif 80 < random_num <= 89:
			print "Score:",random_num,"; Your grade is B"
		elif 90< random_num <= 100:
			print "Score:",random_num,"; Your grade is A"
	print "End of the program. Bye!"
score_grades()