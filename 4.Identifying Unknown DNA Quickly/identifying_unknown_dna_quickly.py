file = open("rosalind_gc.txt")

codes = []
sequences = []
percentages = []

aux = []

for line in file:
    if ">" in line:
        codes.append(line[1:])
        if aux!=[]:
            sequences.append("".join(aux))
            aux = []
    else:
        aux.append(line[:-1])
sequences.append("".join(aux))

for sequence in sequences:
    gc_count = 0.0
    for d in sequence:
        if d=="G" or d=="C":
            gc_count+=1.0
    percentages.append((gc_count/len(sequence))*100)

i = percentages.index(max(percentages))

print(str(codes[i]) + str(percentages[i]))
