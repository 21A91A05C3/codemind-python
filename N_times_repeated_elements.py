n=int(input())
arr=list(map(int,input().split()))
a=int(input())
c=0
l=[]
for i in set(arr):
    if arr.count(i)==a:
        l.append(i)
        c+=1
if(c>0):
    print(*l)
else:
    print(-1)
