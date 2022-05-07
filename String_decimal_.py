n=int(input())
c=0
for i in range(n):
    c=0
    a=input()
    for j in a:
        if j .isdigit():
            c+=1
    if len(a)==c:
        print("True")
    else:
        print("False")