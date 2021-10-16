def nonConstructibleChange(coins):
	coins.sort()
    # Write your code here.
    changeable=0
	for coin in coins:
		if coin>changeable+1:
			return changeable+1
		changeable+=coin
	return changeable+1
	
