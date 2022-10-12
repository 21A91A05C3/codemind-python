n=input().split()
c=ord(n[-1][0])
ans=n[-1][0]
for i in n[-1]:
    if ord(i)<c:
        c=ord(i)
        ans=i
if ans.upper() and ans.lower() in n[-1]:
    print(ans.lower())
else:
    print(ans)
        
# n=input().split()
# c=ord(n[-1][0])
# ans=n[-1][0]
# for i in n[-1]:
#     if ord(i)<c:
#         c=ord(i)
#         ans=i
# if ans.isupper() and ans.lower() in n[-1]:
#     print(ans.lower())
# else:
#     print(ans)