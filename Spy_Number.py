a=int(input())
sum=0
product=1
while(a>0):
    d=a%10
    sum=sum+d
    product=product*d
    a=a//10
if(sum==product):
    print("Spy Number")
else:
    print("Not Spy Number")

