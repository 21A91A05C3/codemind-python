n=int(input())
c=0
for i in range(n):
    c=0
    a=input()
    for j in a:
        if j .isdigit():
            c+=1
    if c>0:
        print("Yes")
    else:
        print("No")