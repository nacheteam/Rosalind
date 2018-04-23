MIN_LENGTH = 4
MAX_LENGTH = 12

def reverseComplement(data):

    reverse_complement = []

    for i in range(len(data)):
        if data[i]=="A":
            reverse_complement.append("T")
        elif data[i]=="T":
            reverse_complement.append("A")
        elif data[i]=="G":
            reverse_complement.append("C")
        elif data[i]=="C":
            reverse_complement.append("G")

    return ("".join(reverse_complement[::-1]))

file = open("rosalind_revp.txt","r")

dna = ""
findings = []

for line in file:
    if not ">" in line:
        dna+=str(line[:-1])

for i in range(MIN_LENGTH,MAX_LENGTH+1):
    for j in range(len(dna)-i+1):
        if dna[j:j+i]==reverseComplement(dna[j:j+i]):
            findings.append([j+1,i])

for f in findings:
    print(str(f[0]) + " " + str(f[1]))
