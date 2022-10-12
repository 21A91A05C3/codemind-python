def check(s):
    v="aeiou"
    c=0
    n=len(s)
    for i in range(len(s)//2):
        if (s[i] in v and s[n-i-1] not in v) or (s[i] not in v and s[n-i-1] in v):
            c+=1
    return c
n=input().lower()
x=0
for i in n.split():
    x+=check(i)
print(x)