filename = "input.txt"
summa = 0
with open(filename, "r") as f:
    for line in f:
        line = line.strip()
        # print(line)
        minFirst = -1
        minSecond = -1
        for i in range(len(line)):
            number = int(line[i])
            if i != len(line)-1 and number>minFirst:
                minFirst = number
                minSecond = int(line[i+1])
            elif number > minSecond:
                minSecond = number
        summa += int(f"{minFirst}{minSecond}")
        print(int(f"{minFirst}{minSecond}"))
print(summa)