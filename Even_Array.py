n=int(input())
l=list(map(int,input().split()))
c=0
d=0
for i in l:
    if i%2==0:
        c+=1
    else:
        d+=1
if d==0 and c>0:
    print("True")
else:
    print("False")