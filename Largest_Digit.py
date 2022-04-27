n=int(input())
i=len(str(n))
b=0
for x in range(i):
    if(n%10>b):
        b=n%10
        n=n//10
    else:
        n=n//10
print(b)