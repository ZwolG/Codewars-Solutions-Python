'''
Character with longest consecutive repetition

DESCRIPTION:
For a given string s find the character c (or C) with longest consecutive repetition and return:

[c, l]
where l (or L) is the length of the repetition. If there are two or more characters with the same l return the first in order of appearance.

For empty string return:

["", 0]
'''

from itertools import groupby
def longest_repetition(chars):
    if not chars:
        return ('', 0)
    return sorted([(i, len(list(j))) for i, j in groupby(chars, key=lambda x: x[0])], key=lambda x: x[1], reverse= True)[0]
