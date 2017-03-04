def hammingDistance(stringA,stringB) :
        count = 0
        for i in range(len(stringA)):
                if stringA[i] != stringB[i]  :
                        count += 1
        return count

a = raw_input()
b = raw_input()
print hammingDistance(a,b)

