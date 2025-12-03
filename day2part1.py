filename = "input.txt"
res = []
with open(filename, "r") as f:
    for line in f:
        line = line.strip()        # remove newline
        if not line:
            continue               # skip empty lines
        # print(line)
        split_comma = line.split(",")
        # print(split_comma)
        
        for x in split_comma:
            split = x.split("-")
            count = 0
            if split == [""]:
                continue
            for i in range(int(split[0]),int(split[1])+1,1):
                stri = str(i)
                if len(stri)%2==0 and stri[:len(stri)//2]==stri[len(stri)//2:]:
                    res.append(i)

            # print(split)
print(sum(res))