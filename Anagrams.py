n=input().lower()
m=input().lower()
v=0
for i in n:
    if i in m:
        v+=1
if v==len(n):
    print("True")
else:
    print("False")