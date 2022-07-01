n=int(input())
temp=n
a=0
b=1
l=[0,1]
while(temp):
    c=a+b
    l.append(c)
    a=b
    b=c
    temp-=1
for i in range(n,-1,-1):
    if i in l:
        back=i
        break
for i in range(n,2*n+1):
    if i in l:
        front=i
        break
if (n-back)<(front-n):
    print(back)
elif (n-back)>(front-n):
    print(front)
else:
    print(back,front)
    