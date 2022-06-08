from math import sqrt
n=int(input())
temp=n
c=0
for i in range(n):
    for j in range(n):
        if (i**2)+(j**2)==temp:
            c+=1
if c==0:
    print("False")
else:
    print("True")
          
          