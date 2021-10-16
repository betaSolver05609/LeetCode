#Monotonic Array

#Linear Time

def isMonotonic(array):
    # Write your code here.
	spinLock1=True;
	spinLock2=True;
	if len(array)==0 or len(array)==1:
		return True
	lastElement=array[0];
	for i in range(1, len(array)):
		if spinLock1==False and spinLock2==False:
			return False
		if array[i]>lastElement:
			spinLock2=False;
		elif array[i]<lastElement:
			spinLock1=False;
		lastElement=array[i]
	
	if spinLock1==False and spinLock2==False:
		return False
	return True
    
