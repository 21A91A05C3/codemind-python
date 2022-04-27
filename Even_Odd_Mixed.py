n=int(input())
m=0
k=0
c=0
while n>0:
    r=n%10
    m+=1
    if r%2==0:
        c+=1
    else:
        k+=1
    n=n//10
if(m==c):
    print("Even")
elif(m==k):
     print("Odd")
else:
     print("Mixed")
    