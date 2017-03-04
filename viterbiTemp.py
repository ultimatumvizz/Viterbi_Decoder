import string 
def nextStateConvolutionTable(polNum) :
	liz = []
	iniState = "0" * polNum
	State = iniState[:polNum-1] + "1"
	print State
	liz.append(State)
	i = polNum -1
	while i != -1 :
			liz.append(State)
			if  State[i] == "1":
				State = string.replace(State,State[i],"0")
				i = polNum -1
				liz.append(State)
			if 	State[i] == "0" :
				State = string.replace(State,State[i],"1")
				i-=1
				liz.append(State)
	print liz
	return 
					
def main() :
	nextStateConvolutionTable(input())

if __name__ == '__main__':
	main()
