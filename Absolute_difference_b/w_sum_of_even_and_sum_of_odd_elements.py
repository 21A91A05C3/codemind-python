n=int(input())
c=0
e=0
arr=list(map(int,input().strip().split()))[:n]
for i in range(0,len(arr)):
    if arr[i]%2==0:
        c=c+arr[i]
    elif arr[i]%2!=0:
        e=e+arr[i]
print(abs(e-c))