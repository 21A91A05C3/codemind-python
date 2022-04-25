a=int(input())
sq=a*a
rev=0
rev1=0
while(a>0):
    d=a%10
    rev=rev*10+d
    a=a//10
sq1=rev*rev
while(sq1>0):
    d1=sq1%10
    rev1=rev1*10+d1
    sq1=sq1//10
if(sq==rev1):
    print("True")
else:
    print("False")

    