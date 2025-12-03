filename = "input.txt"
summa = 0


with open(filename, "r") as f:
    for line in f:
        line = line.strip()
        top12 = list(range(len(line) - 12, len(line)))
        previus = -1
        for j in range(len(top12)):
            for i in range(top12[j],previus,-1):
                if int(line[i])>= int(line[top12[j]]):
                    top12[j]=i
            previus = top12[j]
        number = int("".join(str(line[x]) for x in top12))
        summa+=number
print(summa)