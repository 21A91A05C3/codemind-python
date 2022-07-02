k=int(input())
n=list(map(int,input().split()))
m=len(n)//2
sum=0
for i in range(0,m):
    sum=sum+n[i]
sum1=0
for i in range(m,len(n)):
    sum1=sum1+n[i]
print(abs(sum-sum1))