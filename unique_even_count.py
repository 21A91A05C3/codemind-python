n=int(input())
Sum=0
arr=list(map(int,input().strip().split()))[:n]
for i in range(0,len(arr)):
    c=0
    for j in range(i+1,len(arr)):
        if arr[i]==arr[j] and i!=j:
            c+=1
    if c==0:
        if arr[i]%2==0:
            Sum+=1
print(Sum)