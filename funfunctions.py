def odd_even():
  for i in range(0,2000):
    if i%2==0:
      print (i, "is an even number")
    if i%2==1:
      print (i, "is an odd number")

def multiply(a,b):
    for i in a(0,len(a)):
        a[i]*=b
    print a


def layer(arr):
  print(arr)
  new=[]
  for z in arr:
    val=[]
    for i in range(0,z):
      val.append(1)
    new.append(val)
  return new

x=layer(multiply([2,4,5],1))
print x
