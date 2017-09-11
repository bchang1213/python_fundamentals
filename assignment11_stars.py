def draw_stars(arr):
	length = len(arr)
	for value in range(length):
		arrayvalue = arr[value]
		if type(arrayvalue) == int:
			print "*" * arr[value]
		elif type(arrayvalue) == str:
			print arrayvalue[0] * len(arrayvalue)

x = [4, 6, 1, 3, 5, 7, "zippdpsdfkajlsdkfjlskadjflaksjdflkas"]
draw_stars(x)