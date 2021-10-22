#Staircase Recursive Solution

def staircaseTraversal(height, maxSteps):
    # Write your code here.
	return stepsrequired(height, maxSteps)
	pass

def stepsrequired(height, maxSteps):
	if height<=1:
		return 1
	else:
		print(height)
		numberOfWays=0
		for step in range(1, min(height, maxSteps)+1):
			numberOfWays=numberOfWays+stepsrequired(height-step, maxSteps)
	return numberOfWays
		

#Staircase memoized Solutions

def staircaseTraversal(height, maxSteps):
    # Write your code here.
	return stepsrequired(height, maxSteps, {0: 0, 1:1})
	pass

def stepsrequired(height, maxSteps, memoize):
	if height<=1:
		return 1
	else:
		numberOfWays=0
		for step in range(1, min(height, maxSteps)+1):
			numberOfWays=numberOfWays+stepsrequired(height-step, maxSteps, memoize)
		memoize[height]=numberOfWays
		print(memoize)
	return numberOfWays
		

#Staircase Iterative Solutions

def staircaseTraversal(height, maxSteps):
    # Write your code here.
	a=[0 for i in range(height+1)]
	a[0]=1
	a[1]=1
	
	for currentHeight in range(2, height+1):
		step=1
		while step<=currentHeight and step<=maxSteps:
			a[currentHeight]=a[currentHeight]+a[currentHeight-step]
			step+=1
	print(a)
	return a[height]


			 