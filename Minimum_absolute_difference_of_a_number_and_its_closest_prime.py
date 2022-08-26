def prime(i):
    if i==1:
        return 0
    c=0
    for j in range(1,i+1):
        if i%j==0:
            c+=1
    if c==2:
        return 1
    else:
        return 0
a=int(input())
for i in range(a,1,-1):
    if prime(i)==1:
        d=i
        break
for i in range(a+1,a**2):
    if prime(i)==1:
        k=i
        break
if(abs(a-d)>abs(a-k)):
    print(abs(a-k))
else:
    print(abs(a-d))
