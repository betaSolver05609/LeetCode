#Min Rewards

def minRewards(scores):
    # Write your code here.
	rewards=[1 for i in range(len(scores))]
	a=scores
	#Left to Right Iteration
	for i in range(1, len(scores)):
		if a[i-1]<a[i]:
			rewards[i]=rewards[i-1]+1
	#Right to Left Iteration
	print(a)
	print(rewards)
	for i in reversed(range(len(a)-1)):
		#print(i)
		if a[i+1]<a[i]:
			rewards[i]=max(rewards[i], rewards[i+1]+1)
	print(rewards)
    return sum(rewards)
