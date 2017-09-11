#Multiples
# Part I - Write code that prints all the odd numbers from 1
# to 1000. Use the for loop and don't use a list to do this
# exercise.

#Prints all odd numbers between 1 and 1000.
for i in range(1,1001):
	if i%2 != 0:
		print i

# Part II - Create another program that prints all the
# multiples of 5 from 5 to 1,000,000.

# for x in range(5,1000001):
	if x%5 == 0:
		print x


# Sum List
# Create a program that prints the sum of all the values in
# the list:

a = [1, 2, 5, 10, 255, 3]
sum = 0
length = len(a)
for y in range(0,length):
	sum += a[y]
print sum


# Average List
# Create a program that prints the average of the values in
# the list: 

sum2 = 0
b = [1, 2, 5, 10, 255, 3]
length2 = len(b)
for z in range(0,length2):
	sum2 += b[z]
avg = sum2/length2
print avg
