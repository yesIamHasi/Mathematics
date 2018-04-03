# Implementing Bisection method in python
# For linear functions only

def bisection(func, a, b):
    ''' Finds root in the interval [a,b] by Bisection method '''
    while True:
        # Find F(a)
        x = a
        F_a = eval(func)
        # Find F(b)
        x = b
        F_b = eval(func)

        # If F(a) * F(b) is negative then the root exist in the interval
        # [a, b]
        if F_a * F_b < 0:
            # Find Midpoint
            c = (a+b)/2
            # Find F(c)
            x = c
            F_c = eval(func)
        else:
            print 'No solution exist in interval', (a,b)

        # Shorten the interval [a,b]
        if F_c*F_a < 0:
            b = c
        if F_c*F_b < 0:
            a = c

        # If c satisfies the function then c is the root
        x = c
        F_c = eval(func)
        if F_c == 0:
            print 'Root:', c
            break

# Let's run

bisection('2*x+2', 100, -102)

