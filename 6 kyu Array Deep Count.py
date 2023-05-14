'''
Array Deep Count

DESCRIPTION:
You are given an array. Complete the function that returns the number of ALL elements within an array, including any nested arrays.

Examples
[]                   -->  0
[1, 2, 3]            -->  3
["x", "y", ["z"]]    -->  4
[1, 2, [3, 4, [5]]]  -->  7
'''

def deep_count(a):
    numbers = []
    number = []
    count = 0
    a = str(a)
    for i in a:
        if i.isalnum():
            number.append(i)
        elif number:
            numbers.append(''.join(number))
            number = []
    for i in range(1, len(a) -1):
        if a[i] == '[' and a[i - 1] != '\'':
            count += 1
    count = count + len(numbers)
    return count
