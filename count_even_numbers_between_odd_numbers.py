m=int(input())
l=list(map(int,input().split()))
v=0
for i in range(1,m-1):
    if l[i-1]%2!=0 and l[i+1]%2!=0:
        if l[i]%2==0:
            v+=1
print(v)
    