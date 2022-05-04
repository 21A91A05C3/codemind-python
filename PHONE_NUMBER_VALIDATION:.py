str=input()
for i in str:
    if(len(str)==10):
        if(str[0]!=0):
            print("Valid")
            break
        else:
            print("Inavalid")
else:
    print("Invalid")