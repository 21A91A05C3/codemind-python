k,m=map(int,input().split())
l=[]
arr=list(map(int,input().split()))[:k]
arr1=list(map(int,input().split()))[:m]
for i  in arr:
    if  i in arr1:
        if i not in l:
            l.append(i)
print(*l)
