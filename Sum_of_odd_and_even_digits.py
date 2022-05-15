n=int(input())
c=0
e=0
arr=list(map(int,input().strip().split()))[:n]
for i in range(0,len(arr)):
    if i%2==0:
        c=c+arr[i]
    elif i%2!=0:
        e=e+arr[i]

if((e-c)==0):
    print("YES")
else:
    print("NO")
