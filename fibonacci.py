n=int(input())
a=0
b=1
print(a,b,end=' ')
sum=a+b
for i in range(2,n):
    print(sum,end=' ')
    a=b
    b=sum
    sum=a+b