n=int(input())
arr=list(map(int,input().split()))
l=[]
a=[]
for i in arr:
    if i not in l:
        l.append(i)
    else:
        a.append(i)
print(*a)