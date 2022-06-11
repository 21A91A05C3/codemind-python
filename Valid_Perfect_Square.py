from math import sqrt
def sq(a):
    b=int(sqrt(a))
    if(b*b==a):
        return True
    else:
        return False
n=int(input())
for i in range(n):
    a=int(input())
    print(sq(a))