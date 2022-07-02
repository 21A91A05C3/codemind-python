n=int(input())
l=list(map(int,input().split()))
l=l[::-1]
sum=0
for i in range(n):
    sum=sum+l[i]*2**i
print(sum)
    
    