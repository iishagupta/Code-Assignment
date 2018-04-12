flat_array = []
input_array = [[1, [2], [3]], [4]]


def appendToFlat(arr):
	for element in arr:
		if(type(element) == type([])): # if type of element is array
			appendToFlat(element) # recursively call the function with this element
		else:
			flat_array.append(element)

appendToFlat(input_array)
print(flat_array)