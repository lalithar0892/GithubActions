import sys
num = int(sys.args[1])

a=[]
j=0
for i in range(num):
    a.append(j)
    j+=1
print(f"The Array : {a}")