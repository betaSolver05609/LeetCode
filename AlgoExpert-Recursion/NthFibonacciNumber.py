def getNthFib(n, memo={1:0, 2:1}):
    # Write your code here.
	print(n)
	if n in memo:
		return memo[n]
	else:
		memo[n]=getNthFib(n-1)+getNthFib(n-2)
		return memo[n]

