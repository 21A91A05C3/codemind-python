p,r,t=map(int,input().split())
n=1
a=p*(1+r/100)**(t)
print('{:.2f}'.format(a))