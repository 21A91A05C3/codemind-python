n=int(input())
for i in range(n,0,-1):
    for j in range(n,0,-1):
        if i==j or j==n-i+1 :
            print(i,end=' ')
        else:
            print(' ',end='')
    print('')