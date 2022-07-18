m=int(input())
l=list(map(int,input().split()))
v=0
for i in range(0,m//2):
    print(l[v],l[m-v-1],sep=' ',end=' ')
    v+=1
if m%2==1:
    print(l[m//2],0,sep=' ')