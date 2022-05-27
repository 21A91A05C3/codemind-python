n=int(input())
i=len(str(n))
sq=n**2
last=sq%pow(10,i)
if last==n:
    print("Automorphic Number")
else:
    print("Not an Automorphic Number")
