m=int(input())
a=list(map(int,input().split()))
v=0
for i in range(len(a)):
    if a[i]==1 or a[i]==0:
        v+=1
if v==len(a):
    print("True")
else:
    print("False")