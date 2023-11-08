def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

def absolute_value(a):
    return a if a >= 0 else -a

def factorial(a):
    if a == 0:
        return 1
    return a * factorial(a - 1)

e = 2.718281828459045090795598298427648842334747314453125
pi = 3.141592653589793115997963468544185161590576171875