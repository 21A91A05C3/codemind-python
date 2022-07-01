n=int(input())
l=list(map(int,input().split()))
for i in l:
    rev=0
    while(i):
        d=i%10
        rev=rev*10+d
        i=i//10
    print(rev,end=" ")