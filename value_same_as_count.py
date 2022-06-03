n=int(input())
arr=list(map(int,input().split()))
c=0
for i in set(arr):
    if arr.count(i)==i:
        c+=1
print(c)