n=input()
b=''
for i in n:
    if int(i)%2!=0:
        b=b+str(int(i)**2)
print(b)
