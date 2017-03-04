def permutation(strLen) :
	liz = []
	String = "0" * strLen         #   initial string 
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
	print liz
	return 	

#permutation(int(sys.argv[1]))				
