reading_instructions = True
listOfTuples = []
count=0
with open("input.txt", "r") as file:
    for i,line in enumerate(file):
        
        line = line.strip()
        if line == "":
            reading_instructions = False
            continue
        if reading_instructions:
            two_numbers = line.split("-")
            listOfTuples.append((int(two_numbers[0]),int(two_numbers[1])))
        else:
            for touple_ in listOfTuples:
                if int(line)>= touple_[0] and int(line)<= touple_[1]:
                    count+=1
                    break
print(count)