a=int(input())
sum=0
temp=a
for i in range(1,a):
    
    if a%i==0:
        sum=sum+i
if(temp==sum):
    print("True")
else:
    print("False")