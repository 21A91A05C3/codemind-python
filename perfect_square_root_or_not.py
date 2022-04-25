import math
a=int(input())
root=math.sqrt(a)
if int(root +0.9999) ** 2== a:
    print("True")
else:
    print("False")