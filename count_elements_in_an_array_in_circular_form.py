n=int(input())
arr=list(map(int,input().split()))
c=t=0
for j in range(n):
    if (j>=n-2):
        p2=t
        t+=1
    else:
        p2=j+2
    if(arr[j]%2!=0 and arr[p2]%2==0) or (arr[j]%2==0 and arr[p2]%2!=0) :
        c+=1
print(c)