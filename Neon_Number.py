a=int(input())
temp=a
k=a*a
sum=0
while(k>0):
    d=k%10
    k=k//10
    sum=sum+d
if(temp==sum):
    print("Neon Number")
else:
    print("Not Neon Number")