#Find and Replace
# words = "It's thanksgiving day. It's my birthday,too!"

# replace = words.find("day")
# print replace

# new = words.replace("day", "month")
# print new

#Min and Max
# x = [2,54,-2,7,12,98]

# minimum = min(x)
# print "The minimum value of the given list is" , minimum

# maximum = max(x)
# print "The maximum value of the given list is" , maximum

#First and Last
# x = ["hello",2,54,-2,7,12,98,"world"]
# y = []

# # firstval = x[:1]
# firstval2 = x[0]
# # print firstval
# print firstval2

# lengthx = len(x)
# lastval = x[lengthx-1] 
# print lastval

# y.append(firstval2)
# y.append(lastval)
# print y

#New List
x = [19,2,54,-2,7,12,98,32,10,-3,6]
x.sort()
print x
xlength = len(x)
y = x[:xlength/2]
print y
z = x[xlength/2:]
print z

z.insert(0,y)
print z