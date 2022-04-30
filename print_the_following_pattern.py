n=int(input())
for i in range(1,n+1):#no.rows
    for j in range(1,n-i+2):#no.col
        print(j,end='')
    print('')