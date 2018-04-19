file = open("rosalind_rna.txt","r")
data = file.read()
rna = []

for d in data:
	if d=="T":
		rna.append("U")
	else:
		rna.append(d)

rna = "".join(rna)
print(rna)
