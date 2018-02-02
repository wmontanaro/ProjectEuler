'''
Project Euler Problem 66:

Consider quadratic Diophantine equations of the form:

x^2 – Dy^2 = 1

For example, when D=13, the minimal solution in x is 649^2 – 13×180^2 = 1.

It can be assumed that there are no solutions in positive integers when D is
square.

By finding minimal solutions in x for D = {2, 3, 5, 6, 7}, we obtain the
following:

3^2 – 2×2^2 = 1
2^2 – 3×1^2 = 1
9^2 – 5×4^2 = 1
5^2 – 6×2^2 = 1
8^2 – 7×3^2 = 1

Hence, by considering minimal solutions in x for D ≤ 7, the largest x is
obtained when D=5.

Find the value of D ≤ 1000 in minimal solutions of x for which the largest
value of x is obtained.

'''

#The below works, but it is too slow (try find_minx(61) for example)
'''
def f(x,y,d):
    result = (x**2) - (d*(y**2))
    return result

def find_minx(d):
    x = 0
    y = 1
    result = 0
    while result != 1:
        x += 1
        result = f(x,y,d)
        while result > 0:
            if result == 1:
                return x
            y += 1
            result = f(x,y,d)

def main(d):
    minx = -float("inf")
    maxx = -float("inf")
    for i in range(1, d+1):
        #print("out testing " + str(i))
        if int(i ** 0.5) != i ** 0.5: #skip squares
            #print("in testing " + str(i))
            minx = find_minx(i)
        if minx > maxx:
            maxx = minx
    return maxx
'''
                

print("Problem 66 solution: ")
