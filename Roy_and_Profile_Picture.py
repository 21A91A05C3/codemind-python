l=int(input())
n=int(input())
for i in range(n):
    x,y=map(int,input().split())
    if(x<l or y<l):
        print("UPLOAD ANOTHER")
    elif(x==y or y==x):
        print("ACCEPTED")
    else:
        print("CROP IT")