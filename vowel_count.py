def string_count(str):
    count=0
    vowel=set('aeiouAEIOU')
    for alphabet in str:
        if alphabet in vowel:
            count+=1
    print(count)
str=input()
string_count(str)
