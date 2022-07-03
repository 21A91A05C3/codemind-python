n=int(input())
l=list(map(int,input().split()))
sum=0
i=1
for i in l:
    if i%2!=0:
        sum=sum+i
    else:
        break
print(sum)