l=list(map(int,input().split()))
max=0
for i in range(len(l)):
    for j in range(i+1,len(l)):
        if max<l[i]*l[j]:
            max=l[i]*l[j]
            a=l[i]
            b=l[j]
print((a-1)*(b-1))
            