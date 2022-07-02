n=int(input())
l=list(map(int,input().split()))
a=[]
for i in range(n):
    c=0
    while l[i]>0:
        d=l[i]%10
        l[i]=l[i]//10
        c+=1
    a.append(c)
print(a.count(min(a)))