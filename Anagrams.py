n=input().lower()
m=input().lower()
c=0
for i in n:
    if i in m:
        c+=1
if len(n)==c:
    print("True")
else:
    print("False")