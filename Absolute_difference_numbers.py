n,m=map(int,input().split())
k=str(n)
g=k[:m]#==============first
l=str(k[::-1])
h=l[:m]
d=str(h[::-1])
t=abs(int(g)-int(d))
print(t)