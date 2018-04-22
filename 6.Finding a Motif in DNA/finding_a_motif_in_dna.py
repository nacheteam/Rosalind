file = open("rosalind_subs.txt","r")

dna_strings = []

for line in file:
    dna_strings.append(line[:-1])

dna_substring_len = len(dna_strings[1])
positions = []

for i in range(len(dna_strings[0])-dna_substring_len):
    if dna_strings[1] == dna_strings[0][i:i+dna_substring_len]:
        positions.append(i+1)

for pos in positions:
    print(str(pos)+" ",end="",flush=True)
