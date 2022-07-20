def maxi(k):
    if len(k)==2:
        return max(k)
    elif len(k)>=3:
        k.remove(max(k))
        k.remove(max(k))
    return max(k)
        
n=int(input())
l=list(map(int,input().split()))
k=set(l)
print(maxi(k))