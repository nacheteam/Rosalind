file = open("rosalind_revc.txt","r")
data = file.read()
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

print("".join(reverse_complement[::-1]))
