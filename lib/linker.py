import permutation
def convolution(polynomial,string) :
	polyBin = "0" *(len(string)-len(bin(polynomial)[2:])) + bin(polynomial)[2:]
	finBit = 0 
	for i in range(len(string)) :
		if polyBin[i] == "1" :
			finBit += int(string[i]) 
		finBit %= 2
	return str(finBit)	

def linkingFunc(polList,winSize) :
        polyPossibles =  permutation.permutation(len(polList))
        winPossibles  =  permutation.permutation(winSize)
        keyList   = { string : [] for string in polyPossibles }
        winList   = { string : [] for string in winPossibles }
        for string in winPossibles :
                strip = ""
                for i in range (len(polList)) :
                        strip += convolution(polList[i],string)
                keyList[strip].append(string)
                winList[string].append(strip)
#        for key in keyList.keys() :
#                if keyList[key] == [] :
#                        del keyList[i]
	return keyList,winList
	
