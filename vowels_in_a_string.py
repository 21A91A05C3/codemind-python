n=input()
m=input()
for i in range(len(n)):
    if n[i]==m:
        print("True")
        print(i)
        break
else:
    print("False")