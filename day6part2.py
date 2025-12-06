import re
import numpy as np
tab = []
with open("input.txt", "r") as file:
    for i,line in enumerate(file):      
        line = list(line.strip("\n"))
        tab.append(line)
        
tab = np.flipud(np.array(tab).T)
temp_tab = []
summa = 0
for row in tab:
    row = "".join([x for x in row if x != " "])
    if row == "":
        continue
    if row[-1]=="*":
        temp_tab.append(int(row[:-1]))
        summa += np.prod(temp_tab)
        temp_tab = []
        continue
    elif row[-1]=="+":
        temp_tab.append(int(row[:-1]))
        summa += np.sum(temp_tab)
        temp_tab = []
        continue
    temp_tab.append(int(row))
print(summa)



