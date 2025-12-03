filename = "input.txt"
res = []
with open(filename, "r") as f:
    for line in f:
        line = line.strip()
        if not line:
            continue               
        split_comma = line.split(",")
        
        for x in split_comma:
            split = x.split("-")
            count = 0
            if split == [""]:
                continue
            for i in range(int(split[0]),int(split[1])+1,1):
                stri = str(i)
                for i in range(1,len(stri)+1,1):
                    if len(stri)%i==0:
                        chunk_size = len(stri) // i
                        # split into n chunks
                        chunks = [stri[i:i+chunk_size] for i in range(0, len(stri), chunk_size)]

                        # check if all chunks are equal
                        all_equal = all(chunk == chunks[0] for chunk in chunks)
                        if all_equal and len(chunks)>1:
                            res.append(int(stri))
                            break
print(sum(res))

