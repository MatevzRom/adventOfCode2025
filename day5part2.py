def add_interval(intervals, new):
    start, end = new
    result = []
    placed = False

    for a, b in intervals:
        if b < start:
            # interval completely before new
            result.append((a, b))
        elif a > end:
            # interval completely after new
            if not placed:
                result.append((start, end))
                placed = True
            result.append((a, b))
        else:
            # intervals overlap → merge
            start = min(start, a)
            end = max(end, b)

    if not placed:
        result.append((start, end))

    return result

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
            listOfTuples = add_interval(listOfTuples,(int(two_numbers[0]),int(two_numbers[1])))
        else:
            break
for touple_ in listOfTuples:
    count+= touple_[1]-touple_[0]+1
print(count)