n=int(input())
temp=n
l=[]
while n>0:
    d=n%10
    l.append(d)
    n=n//10
for ele in l:
    if l.count(ele)>1:
        print("Not Unique Number")
        break
else:
    print("Unique Number")