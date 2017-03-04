import textwrap

def permutation(strLen) :
        liz = []
        String = "0" * strLen         
        liz.append(String)
        i = strLen - 1
        while i != -1 :
                if  String[i] == "0" :
                        String = String[:i] + "1" + String[i+1:]
                        liz.append(String)
                        i = strLen - 1
                if String[i] == "1" :
                        String = String[:i] + "0" + String[i+1:]
                        i = i - 1
        return liz

def convolution(polynomial,string) :
        polyBin = "0" *(len(string)-len(bin(polynomial)[2:])) + bin(polynomial)[2:]
        finBit = 0
        for i in xrange(len(string)) :
                if polyBin[i] == "1" :
                        finBit += int(string[i])
                finBit %= 2
        return str(finBit)

def linkingFunc(polList,polyPossibles,winPossibles) :
        #polyPossibles =  permutation(len(polList))
        #winPossibles  =  permutation(winSize)
        keyList   = { string : [] for string in polyPossibles }
        winList   = { string : [] for string in winPossibles }
        for string in winPossibles :
                strip = ""
                for i in xrange (len(polList)) :
                        strip += convolution(polList[i],string)
                keyList[strip].append(string) 
                winList[string].append(strip)
#	for key in keyList.keys() :
#		if keyList[key] == [] :
#			del keyList[i]   	
	return keyList,winList

def nextStateTable(possibleElements):
	table = dict.fromkeys(possibleElements)
	for string in possibleElements:
		table[string] =  [ string[1:] + "0" , string[1:] + "1"  ]
	return table
 	
def hammingDistance(stringA,stringB) :
	count = 0
	for i in range(len(stringA)):
		if stringA[i] != stringB[i]  :
			count += 1
	return count
def listMinHammingDist(givenString,stringList) :
        Liza = [stringList[0]]
        minDist = hammingDistance(givenString,stringList[0]) 
        for i in xrange(1,len(stringList)) :
                tempDist = hammingDistance(givenString,stringList[i])
                if tempDist == minDist :
                        Liza.append(stringList[i])
                if tempDist < minDist :
                        Liza = [stringList[i]]   
			minDist = tempDist 
			                    
        return Liza,minDist
def nonEmptyKeys(keyList):
	liza = []
	for key in keyList.keys() :
		if keyList[key] != [] :
			liza.append(key)
	return liza	        
def viterbiSearchAlgo(mssgBit,segmentList,keyList,nextState):
	mssg = ""
	if segmentList == [] :
		return  ""
	if keyList[segmentList[0]] == [] :
		segments,minDist = listMinHammingDist(segmentList[0],nonEmptyKeys(keyList))
		for segment in segments :	
			 if mssgBit[1:] + "0" in keyList[segment] :
                 		mssg +=  "0" + viterbiSearchAlgo(nextState[mssgBit][0],segmentList[1:],keyList,nextState)
        		 elif mssgBit[1:] + "1" in keyList[segment] :
                		mssg +=  "1"  + viterbiSearchAlgo(nextState[mssgBit][1],segmentList[1:],keyList,nextState)
        		 else :
                		return  "DD"
	elif mssgBit[1:] + "0" in keyList[segmentList[0]] :
		 mssg +=  "0" + viterbiSearchAlgo(nextState[mssgBit][0],segmentList[1:],keyList,nextState)
	elif mssgBit[1:] + "1" in keyList[segmentList[0]] :
		mssg +=  "1"  + viterbiSearchAlgo(nextState[mssgBit][1],segmentList[1:],keyList,nextState) 
	else :
		return  "D"
	return mssg

def viterbiSearch2(mssgBit,segmentList,keyList,nextState,winList):
	
	if segmentList == [] :
		return [0,[""]]
	#print winList[mssgBit][0] , segmentList[0] ,
	hammingDist =  hammingDistance(winList[mssgBit][0],segmentList[0])	
	#print hammingDist ,
	listA = viterbiSearch2(nextState[mssgBit][0],segmentList[1:],keyList,nextState,winList)
	listB = viterbiSearch2(nextState[mssgBit][1],segmentList[1:],keyList,nextState,winList)
	
	if listA[0] > listB[0] :
		return [listB[0]+hammingDist,["1" + element for element in listB[1]]]
	elif listA[0] == listB[0] :
		return [listB[0]+hammingDist,["0" + element for element in listA[1]]+["1" + element for element in listB[1]]]
	else :
	   	return [listA[0]+hammingDist,["0" + element for element in listA[1]]]
	
def viterbiDecoder(encryptedBits,polyList,windowSize) :

	polyPossibles = permutation(len(polyList))
	winPossibles = permutation(windowSize)	
	#print encryptedBits
	if len(encryptedBits) % len(polyList) != 0 :
		encryptedBits += "0" * (len(polyList) - (len(encryptedBits) % len(polyList)))	
	segmentedBits = textwrap.wrap(encryptedBits,len(polyList))
	print segmentedBits
        nextState = nextStateTable(winPossibles)
        keyList,winList = linkingFunc(polyList,polyPossibles,winPossibles)

 	realMssgList = keyList[segmentedBits[0]]
	#print nextState
	#print nextState['011'][0]
        tempList = keyList[segmentedBits[0]]
	#print tempList
	#print "hello" + str( hammingDistance("000","011"))
	#print keyList
	#print winList
        #for i  in range(len(tempList)) :
	#	tempList[i] += viterbiSearchAlgo(tempList[i],segmentedBits[1:],keyList,nextState)   	
                #minDistElements = listMinHammingDist(segment,[ winList[nextState[state][0]] for state in tempList]+[winList[nextState[state][1]] for state in tempList])       
        flag = 0
	Best = [0,[""]]
	for state in winPossibles:
		temp = viterbiSearch2(state,segmentedBits,keyList,nextState,winList)
		if flag == 0 :
			flag = 1 
			Best = temp
			Best[1] = [state + element for element in  Best[1]]
		elif  temp[0] < Best[0]  :
			Best = temp
			Best[1] = [state + element for element in  Best[1] ]
		elif  temp[0] == Best[0] :
			Best[1] += [state + element for element in temp[1] ]
	Best[1] = [ Best[1][i][:len(segmentedBits)+windowSize-1] for i in range(0,len(Best[1]),2)] 
        #for element in tempList :
	#	if element[-1:] == "D" :
	#		tempList.remove(element)
	#return tempList
	return Best        

def main() :
        
        print "Enter the encoded bits : "
        encryptedBits = raw_input()
        print "Enter the polynomials : "
        polynomials = [int(a) for a in raw_input().split()]
        print "Enter the window size :"
        windowSize = int(raw_input())
        print viterbiDecoder(encryptedBits,polynomials,windowSize)

if __name__ == '__main__':
        main()

				
