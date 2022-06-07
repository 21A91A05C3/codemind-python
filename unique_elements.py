n=int(input())
arr=list(map(int,input().split()))[:n]
l=[]
for i in arr:
    if i not in l:
        l.append(i)
print(*l)
    