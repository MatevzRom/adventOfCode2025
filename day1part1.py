
start = 50
count = 0
with open("input.txt", "r") as file:
    for line in file:
        line = line.strip()   # removes newline and surrounding spaces
        number = int(line[1:])
        if line[0] == 'R':
            start = (start+number)%100
        else:
            start = (start-number)%100
        if start == 0:
            count+=1
        # print(line)
print(count)



