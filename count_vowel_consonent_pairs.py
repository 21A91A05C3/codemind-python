s=input().lower()
c=0
n=len(s)
v='aeiou'
for i in range((n//2)):
    if (s[n-i-1] in v and s[i] not in v and s[i]!=' ') or (s[n-i-1] not in v  and s[i]  in v and s[n-i-1]!=' '):
        c+=1
        # print(s[i],s[n-i-1])
print(c)