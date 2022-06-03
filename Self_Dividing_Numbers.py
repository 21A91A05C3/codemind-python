a=int(input())
b=int(input())
for i in range(a,b+1):
    l=i
    c=0
    k=0
    while(i>0):
        d=i%10
        i=i//10
        c+=1
        if d==0:
            continue
        if l%d==0:
            k+=1
    if c==k:
        
        print(l,end=' ')
        
    
        