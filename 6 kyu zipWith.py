'''
zipWith

DESCRIPTION:
Task
zipWith ( or zip_with ) takes a function and two arrays and zips the arrays together, applying the function to every pair of values.
The function value is one new array.

If the arrays are of unequal length, the output will only be as long as the shorter one.
(Values of the longer array are simply not used.)

Inputs should not be modified.

Examples
zipWith( Math.pow, [10,10,10,10], [0,1,2,3] )      =>  [1,10,100,1000]
zipWith( Math.max, [1,4,7,1,4,7], [4,7,1,4,7,1] )  =>  [4,7,7,4,7,7]

zipWith( function(a,b) { return a+b; }, [0,1,2,3], [0,1,2,3] )  =>  [0,2,4,6]  // Both forms are valid
zipWith( (a,b) => a+b,                  [0,1,2,3], [0,1,2,3] )  =>  [0,2,4,6]  // Both are functions
'''

def add(num1, num2):
    return num1 + num2
def sub(num1, num2):
    return num1 - num2
def pow(num1, num2):
    return num1 ** num2
def mul(num1, num2):
    return num1 * num2

def zip_with(fn,a1,a2):
    result = []
    for num1, num2 in zip(a1, a2):
        result.append(fn(num1, num2))
    return result
