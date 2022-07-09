n=int(input())
l=list(map(int,input().split()))
a=[]
for i in l:
    k=str(i)
    k=len(k)
    a.append(k)
for i in l:
    for j in a:
        if max(a)==len(str(i)):
            print(i,end=' ')
            break