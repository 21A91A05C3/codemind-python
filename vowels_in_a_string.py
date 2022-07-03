n=input()
m=input()
for i in range(0,len(n)-1):
    if m in n:
        print("True")
        print(n.index(m))
        break
    
else:
    print("False")
