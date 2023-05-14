'''
Break camelCase

DESCRIPTION:
Complete the solution so that the function will break up camel casing, using a space between words.

Example
"camelCasing"  =>  "camel Casing"
"identifier"   =>  "identifier"
""             =>  ""
'''

def solution(s):
    indexes = []

    for l in range(len(s)):
        if s[l].isupper():
            indexes.append(l)

    s = [l for l in s]

    for i in range(len(indexes)):
        indexes[i] = indexes[i] + i        

    for i in indexes:
        s.insert(i, ' ')
    
    return ''.join(s)
