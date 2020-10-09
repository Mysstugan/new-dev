def disemvowel(string):
    newstr = string
    vowels = ('a', 'u', 'i', 'o', 'e')
    for x in string:
        if x in vowels:
            newstr = newstr.replace(x,"")
    return newstr

print(disemvowel("Hello my name is tobias"))

#bättre lösning

'''def disemvowel(x):
    return x.translate(None, aeiouAEIOU)'''

#eller med regex

'''import re
def disemvowel(x):
    return re.sub('[aeiou]', '', x, flags = re.IGNORECASE)'''

#med .replace

'''def disemvowel(x):
    for i in "aeiouAEIOU":
        x = x.replace(i,'')
    return x'''
    