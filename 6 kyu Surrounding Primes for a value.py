'''
Surrounding Primes for a value

DESCRIPTION:
We need a function prime_bef_aft() that gives the largest prime below a certain given value n,

befPrime or bef_prime (depending on the language),

and the smallest prime larger than this value,

aftPrime/aft_prime (depending on the language).

The result should be output in a list like the following:

primeBefAft == [befPrime, aftPrime]
If n is a prime number it will give two primes, n will not be included in the result.

Let's see some cases:

primeBefAft(100) == [97, 101]

primeBefAft(97) == [89, 101]

primeBefAft(101) == [97, 103]
Range for the random tests: 1000 <= n <= 200000

(The extreme and special case n = 2 will not be considered for the tests. Thanks Blind4Basics)
'''

def is_prime(num):
    for n in range(2,int(num**0.5) +1):
        if num % n == 0: return False
    return True
def prime_bef_aft(num):
    for i in reversed(range(num)):
        print(i)
        if i == 2:
            befPrime = i
        if is_prime(i):
            befPrime = i
            break


    for i in range(num +1, num*2):
        if is_prime(i):
            aftPrime = i
            break

    return[befPrime, aftPrime]
