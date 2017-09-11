def cointoss():
	import random
	heads = 0
	tails = 0
	coin = ""
	for i in range(5000):
		print 'Attempt #',i,': Throwing a coin...',
		chance = random.randint(1,10)
		if chance >5:
			coin = "head"
			print "'It's a head! ...",
			heads += 1
		else:
			coin = "tails"
			print "'It's a tails! ...",
			tails += 1
		print "Got",heads,"head(s) so far and",tails,"tail(s) so far"
cointoss()

# print 'something',
# print 'else',