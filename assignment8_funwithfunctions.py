# def odd_even():
	for num in range(1,2001):
		if num%2 != 0:
			print "Number is", num, ".", "This is an odd number."
		elif num%2 == 0:
			print "Number is", num, ".", "This is an even number."

odd_even()

def multiply(arr,multiple):
	length = len(arr)
	for value in range(0,length):
		arr[value] *= multiple
	return arr

a = [2,4,5]
b = multiply(a, 3)
print b


def layered_multiples(array):
	new_array = []
	length1 = len(array)
	for multiplevalue in range(0,length1):
		individualarray = []
		for i in range(0,array[multiplevalue]):
			individualarray.append(1)
		new_array.append(individualarray)
	return new_array

x = layered_multiples(b)
print x