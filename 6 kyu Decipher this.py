'''
Decipher this!

DESCRIPTION:
You are given a secret message you need to decipher. Here are the things you need to know to decipher it:

For each word:

the second and the last letter is switched (e.g. Hello becomes Holle)
the first letter is replaced by its character code (e.g. H becomes 72)
Note: there are no special characters used, only letters and spaces

Examples

decipherThis('72olle 103doo 100ya'); // 'Hello good day'
decipherThis('82yade 115te 103o'); // 'Ready set go'
'''

def decipher_this(s):
    result = []
    for word in s.split():
        index = len([int(num) for num in word if num.isdigit()])
        finished_word = chr(int(word[:index])) + word[index:]
        if len(finished_word) > 2:
            l_swap = list(finished_word)
            l_swap[1], l_swap[-1] = l_swap[-1], l_swap[1]
            finished_word = ''.join(l_swap)
        result.append(finished_word)
    return ' '.join(result)
