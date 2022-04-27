a=int(input())
i=len(str(a))
sq=a**2
last=sq%pow(10,i)
if last==a:
    print("Automorphic Number")
else:
    print("Not an Automorphic Number")