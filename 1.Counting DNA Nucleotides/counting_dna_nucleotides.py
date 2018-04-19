file = open("rosalind_dna.txt","r")
data = file.read()
bases = ['A','C','G','T']
countings = [0,0,0,0]
for d in data:
	for i in range(len(bases)):
		if d==bases[i]:
			countings[i]+=1

print(str(countings[0]) + " " + str(countings[1]) + " " + str(countings[2]) + " " + str(countings[3]))

