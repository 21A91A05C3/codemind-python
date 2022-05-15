

string = input()
string=list(string)
for i in range(0,len(string)):
    if string[i]=='6':
        string[i]='9'
        break;
string="".join(string)
print(string)    