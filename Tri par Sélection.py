import os

t=[27,1,2,4,99,42,1,25,556,6,6] 
cpt=len(t) 
for i in range(0,cpt-1): 
    min=i 
    for j in range(i+1,cpt): 
        if t[j] < t[min]: 
            min=j 
    if min != 0: 
        temp=t[min] 
        t[min]=t[i] 
        t[i]=temp 
    for j in range(0,cpt): 
        print(t[j]) 
    print("\n")
os.system("pause");