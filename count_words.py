n=input().split()
m=list(n)
c=0
for i in m:
    if (i[0]=='a' or i[0]=='e' or i[0]=='i' or i[0]=='o' or i[0]=='u' or i[0]=='A' or i[0]=='E' or i[0]=='I'or i[0]=='O'or i[0]=='U') and (i[-1]!='a'or i[-1]!='e' or i[-1]!='i' or i[-1]!='o' or i[-1]!='u' or i[-1]!='A' or i[-1]!='E' or i[-1]!='I' or i[-1]!='O'or i[-1]!='U'):
        c+=1
print(c)