file = open("rosalind_hamm.txt","r")

line_num=0
dna_strings = []
for line in file:
    dna_strings.append(line)

distance = 0
for i in range(len(dna_strings[0])):
    if dna_strings[0][i]!=dna_strings[1][i]:
        distance+=1

print(distance)
