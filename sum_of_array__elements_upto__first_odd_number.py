k=int(input())
l=list(map(int,input().split()))
sum=0
i=0
while l[i]%2==0:
    sum=sum+l[i]
    i+=1
print(sum)