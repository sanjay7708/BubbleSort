def sort(array):
	for i in range(len(array)):
		for j in range(len(array)-1):
			if array[j]>array[j+1]:
				array[j],array[j+1]=array[j+1],array[j]
if __name__=="__main__":
	array=[4,10,5,3,2,1]
	sort(array)
	print(array) 