n=int(input())
l=list(map(int,input().split()))
k=sum(l)/len(l)
print('{:.2f}'.format(k))