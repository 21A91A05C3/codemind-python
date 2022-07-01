a=[0,1]
n=int(input())
b=0
d=1
for i in range(n):
    c=b+d
    a.append(c)
    b=d
    d=c
if n in a:
    print("True")
else:
    print("False")