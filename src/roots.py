import math

def quadratic_roots(a,b,c):
    #quadratic_roots calculates how many roots a function has and calculates the roots.
    v = (b*b)-4*a*c
    #v is the discrimnant
    print('\n''Equation: ' + str(a) + 'x^2 + '+str(b)+'x + '+ str(c) )
    if v < 0:
        print('No roots', '\n')
    elif v == 0:
        r = (-b + math.sqrt(v))/(2*a)
        #r is the one root
        print('One Root: ', '\n', 'x = ' , str(r),'\n')
    elif v > 0:
        r1 = (-b + math.sqrt(v))/(2*a)
        #r1 is the first root
        r2 = (-b - math.sqrt(v))/(2*a)
        #r2 is the second root
        print('Two Roots: ', '\n' 'x = ' , str(r1),'\n' 'x = ' , str(r2),'\n')

def main():
    quadratic_roots(-1,-5,1)
    quadratic_roots(-4,-1,3)
    quadratic_roots(5,1,1)
    quadratic_roots(-2,0,-2)
    quadratic_roots(5,-4,-1)
    quadratic_roots(-1,8,-16)
    quadratic_roots(1,-12.6, 39.69)
    quadratic_roots(1,-1.348,-5.62688)
    quadratic_roots(2,20,25)
    quadratic_roots(-1,456,-52016)

if __name__ == "__main__":
    main()