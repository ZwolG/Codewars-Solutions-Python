'''
Irreducible Sum of Rationals

DESCRIPTION:
You will have a list of rationals in the form

lst = [ [numer_1, denom_1] , ... , [numer_n, denom_n] ]
or

lst = [ (numer_1, denom_1) , ... , (numer_n, denom_n) ]
where all numbers are positive integers. You have to produce their sum N / D in an irreducible form: this means that N and D have only 1 as a common divisor.
'''
from math import gcd
def sum_fracts(lst):
    print(lst)
    denominators = [x[1] for x in lst]
    common_denominator = 1
    for i in denominators:
        common_denominator = common_denominator*i//gcd(common_denominator,i)
    number = int(sum([ (common_denominator//x[1]) * x[0] for x in lst ]))
    if number == 0: return None
    if number > common_denominator and number % common_denominator == 0: return int(number // common_denominator)
    return [number, common_denominator] if gcd(number,common_denominator) == 1 else [number//gcd(number,common_denominator),common_denominator//gcd(number,common_denominator)]
