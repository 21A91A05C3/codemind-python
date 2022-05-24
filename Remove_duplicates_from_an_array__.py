n=int(input())
arr=list(map(int,input().split()))[:n]
b=list(set(arr))
print(*b)