n=int(input())
c=0
d=0
arr=list(map(int,input().split()))
for i in arr:
    if i%2==0:
        c+=1
    else:
        d+=1
print(c,d)