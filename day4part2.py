import numpy as np
filename = "input.txt"
table = []
with open(filename, "r") as f:
    for line in f:
        line = line.strip()
        table.append(list(line))
table = np.array(table)
score = 0
while(True):
    indeks_remove = []
    for i in range(table.shape[0]):
        for j in range(table.shape[1]):
            count=0
            if table[i,j]=="@":
                # Check all sides:
                if i>0 and j>0 and table[i-1,j-1]=="@":
                    count+=1
                if i>0 and table[i-1,j]=="@":
                    count+=1
                if j>0 and table[i,j-1]=="@":
                    count+=1
                if i<table.shape[0]-1 and j<table.shape[1]-1 and table[i+1,j+1]=="@":
                    count+=1
                if i<table.shape[0]-1 and table[i+1,j]=="@":
                    count+=1
                if j<table.shape[1]-1 and table[i,j+1]=="@":
                    count+=1
                if i<table.shape[0]-1 and j>0 and table[i+1,j-1]=="@":
                    count+=1
                if i>0 and j<table.shape[1]-1 and table[i-1,j+1]=="@":
                    count+=1
                if count <4:
                    score+=1
                    indeks_remove.append((i,j))
    if indeks_remove == []:
        break
    a, b = zip(*indeks_remove)
    table[a,b] = "x"
print(score)