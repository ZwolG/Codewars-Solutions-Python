'''
Framed Reflection


100th Kata
You are given a message (text) that you choose to read in a mirror (weirdo). Return what you would see, complete with the mirror frame. Example:

'Hello World'

would give:

*********
* olleH *
* dlroW *
*********

Words in your solution should be left-aligned.
'''

def mirror(text):
    text = [x[::-1]  for x  in text.split(' ')]
    l = len(text)
    length = 0
    s = ''
    for i in text:
        length  = max(length, len(i))
    front = (length + 4) * '*' + '\n'
    back = '\n' + (length +4) * '*'

    for i in text:
        diff = length - len(i)
        s += '* ' + i + diff * ' ' + ' *' + ','
    s = '\n'.join((s.split(','))[:-1])
    
    
    return front + s + back
