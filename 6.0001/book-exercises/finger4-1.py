#Write a function isIn that accepts two strings as arguments and returns True if either string occurs anywhere in the other, and False otherwise. Hint: you might want to use the built-in str operation in.

texto = 'abcdef'
text = 'def'

# def isIn(s1, s2):
#     return s2 in s1

# print (isIn(texto, text))

# result: although I think I wasn't supposed to use the in statement, it worked none the less!

# self-challenge: not only check if it is in that, but tell the starting and ending index where s2 matches in s1



def matchStrings(s1,s2):
    def isIn(s1, s2):
        return s2 in s1
    if isIn:
        for d in range(len(s1)):
            if s1[d]  == s2[0] and s1[d+len(s2)-1] == s2[-1]:
                print(f'The second string matches at indexes {d} to {d+len(s2)-1}')
            

    
matchStrings(texto, text)