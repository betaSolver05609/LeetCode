#Array of products

#Optimal Solution O(n) time and O(3*n)=O(n) space

def arrayOfProducts(array):
    # Write your code here.
	leftArray=[1 for i in range(len(array))]
	rightArray=[1 for i in range(len(array))]
	product=[]
	leftProduct=1
	for i in range(len(array)):
		leftArray[i]=leftProduct
		leftProduct=leftProduct*array[i]
	rightProduct=1
	for i in reversed(range(len(array))):
		rightArray[i]=rightProduct
		rightProduct=rightProduct*array[i]
	for i in range(len(array)):
		product.append(leftArray[i]*rightArray[i])
	print(product)
	return product



#My SOlution
#This is not optimal because I am doing a lot of recomputation

def arrayOfProducts(array):
    # Write your code here.
	a=[]
    for i in range(len(array)):
		product=1
		
		if i==0:
			left=-1
		else:
			left=i-1
		if i==len(array)-1:
			right=len(array)
		else:
			right=i+1
		while left>=0:
			product=product*array[left]
			left=left-1
		while right<len(array):
			product=product*array[right]
			right=right+1
		a.append(product)
	print(a)
	return a

