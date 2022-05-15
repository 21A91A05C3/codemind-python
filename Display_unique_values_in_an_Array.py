n=int(input())
arr=list(map(int,input().strip().split()))[:n]
l=[]
v=0
for i in range(0,len(arr)):
    c=0
    for j in range(0,len(arr)):
        if arr[i]==arr[j] and i!=j:
            c+=1
    if c==0:
        l.append(arr[i])
        v+=1
if v!=0:
    print(*l)
else:
    print(-1)