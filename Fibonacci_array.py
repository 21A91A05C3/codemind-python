n=int(input())
l=list(map(int,input().split()))
c=2
for i in range(3,n):
    if l[i]==l[i-2]+l[i-1]:
        c+=1
if c==n-1:
    print("yes")
else:
    print("no")