def permutationNext(string):
		for i in range(len(string)-1,-1,-1):
			if string[i] == 0 :
				string[i] = 1
				break
			if string[i] == 1 :
				string[i] = 0
		return string

def modulo2Addn(stringA,stringB):
	string=""
	for i in range(len(stringB)):
		string+= (stringB+stringA)%2
	return string

def decodingTable(pol1,pol2):
	pol1 = bin(pol1)
	pol2 = bin(pol2)
	liz=[]
	liz.append([000,modulo2Addn("000",pol1)+modulo2Addn("000",pol2))
	string = "001"
	while string != "000" :
		liz.append([string,modulo2Addn(string,pol1)+modulo2Addn(string,pol2)])
		string = permutationNext(string)
	return liz
	
def viterbiDecoder(mssgBits,pol1,pol2) :
	liz = decodingTable(pol1,pol2)

def main():
	print "Enter the message bits : "
	mssgBits = raw_input()
	print "Enter polynomial 1 : "
	pol1 = input()
	print "Enter polynomial 2 : "
	pol2 = input()


if __name__ == '__main__':
	main()
