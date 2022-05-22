def vowel_count(str):
    vowel=set('aeiouAEIOU')
    for alphabet in str.split():
        c=0
        for i in alphabet:
            if i in vowel:
                c+=1
                
        print(c,end=' ')
        
str=input()
vowel_count(str)
