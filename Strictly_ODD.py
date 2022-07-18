n=int(input())
l=list(map(int,input().split()))
v=0
for i in range(0,n):
    if i%2==0 and l[i]%2!=0:
      print("False")
      break
else:
    print("True")
    
