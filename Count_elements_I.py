m,n=map(int,input().split())
l=[]
a=list(map(int,input().split()))[:m]
b=list(map(int,input().split()))[:n]
for i in range(0,len(a)):
    for j in range(0,len(b)):
        if a[i]==b[j]:
            l.append(int(a[i]))
l=list(set(l))
print(len(l))
