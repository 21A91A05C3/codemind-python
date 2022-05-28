n=int(input())

while(1):
    Sum=0
    while n>0:
        d=n%10
        Sum=Sum+d
        n=n//10
    if Sum>0 and Sum<9:
        print(Sum)
        break
    else:
        n=Sum