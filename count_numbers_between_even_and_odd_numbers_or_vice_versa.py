n=int(input())
l=list(map(int,input().split()))
v=0
for i in range(1,n-1):
    if (l[i-1]%2==0 and l[i+1]%2!=0) or (l[i-1]%2!=0 and l[i+1]%2==0):
        v+=1
print(v)