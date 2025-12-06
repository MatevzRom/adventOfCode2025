import re
import numpy as np
tab = []
with open("input.txt", "r") as file:
    for i,line in enumerate(file):      
        line = line.strip()
        line = re.split(r" +", line)
        tab.append(line)
        
tab = np.array(tab)

res = 0
for i in range(tab.shape[1]):
    column = tab[:,i]
    operation = column[-1]
    column = column[:-1].astype(int)
    if operation == "+":
        res+= column.sum()
    elif operation == "*":
        res+= column.prod()
print(res)



