from decimal import Decimal
import random

def NthRoot(k,n, ERROR=10**-15):
    '''
    Finds nth root of a number using a Newton-Raphson algorithm (specific/modified). 
    '''
    # Assume a false value of nth root.
    x = random.randint(1, k)
    while True:
        # Find value of nth root.
        x_n = (1/Decimal(n)) * ( Decimal(n-1)*x + (Decimal(k) / ( Decimal(x)**Decimal(n-1)) ) )
        # Find the error in the value.
        delX = (1/Decimal(n)) * ( (Decimal(k)/(Decimal(x)**Decimal(n-1)) )- Decimal(x))
        x = x_n
        if abs(delX) < ERROR:
            return x_n, delX

if __name__ == '__main__':
    print (NthRoot(5, 10))
