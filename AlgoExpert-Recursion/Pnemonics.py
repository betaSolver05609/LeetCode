#Pnemonics

def phoneNumberMnemonics(phoneNumber):
    # Write your code here.
	currentPnemonics=["0" for i in range(len(phoneNumber))]
	pnemonicsFound=[]
	pnemonicshelper(0, phoneNumber, currentPnemonics, pnemonicsFound)
    return pnemonicsFound


def pnemonicshelper(index, phoneNumber, currentPnemonic, pnemonicsFound):
	if index==len(phoneNumber):
		#print("-------------")
		#print(currentPnemonic)
		pnemonic="".join(currentPnemonic)
		pnemonicsFound.append(pnemonic)
		#print("-------------")
	else:
		element=phoneNumber[index]
		letters=HashMap[int(element)]
		for letter in letters:
			currentPnemonic[index]=letter
			print(currentPnemonic)
			pnemonicshelper(index+1, phoneNumber, currentPnemonic, pnemonicsFound)
		
		
HashMap={
		1: ['1'],
		0: ['0'],
		2: ['a','b','c'],
		3: ['d', 'e', 'f'],
		4: ['g','h', 'i'],
		5: ['j','k','l'],
		6: ['m', 'n', 'o'],
		7: ['p', 'q', 'r', 's'],
		8: ['t','u','v'],
		9: ['w','x','y','z']
	}



def phoneNumberMnemonics(phoneNumber):
    # Write your code here.
	HashMap={
		2: ['a','b','c'],
		3: ['d', 'e', 'f'],
		4: ['g','h', 'i'],
		5: ['j','k','l'],
		6: ['m', 'n', 'o'],
		7: ['p', 'q', 'r', 's'],
		8: ['t','u','v'],
		9: ['w','x','y','z']
	}
	
	pnemonic=[]
	
	for elem in phoneNumber:
		permute=[]
		if int(elem)==0:
			permute.append(0)
			continue
		elif int(elem)==1:
			permute.append(1)
			continue
		else:
			for j in range(len(HashMap[int(elem)])):
				permute.append(HashMap[int(elem)][j])
		pnemonic.append(permute)
	print(pnemonic)
    return []
