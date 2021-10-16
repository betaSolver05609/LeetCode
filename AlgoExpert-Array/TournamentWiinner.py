#Tournament Winner

def tournamentWinner(competitions, results):
    # Write your code here.
    Map={}
	for i in range(len(competitions)):
		if results[i]==1:
			if competitions[i][0] in Map:
				Map[competitions[i][0]]=Map.get(competitions[i][0])+3
			else:
				Map[competitions[i][0]]=3
		if results[i]==0:
			if competitions[i][1] in Map:
				Map[competitions[i][1]]=Map.get(competitions[i][1])+3
			else:
				Map[competitions[i][1]]=3
	return findMax(Map)

				
def findMax(Map):
	m=0
	attribute=""
	for attr, value in Map.items():
		if value>m:
			m=value
			attribute=attr
	return attribute
	
			
			
		
