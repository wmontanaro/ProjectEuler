'''
Project Euler Problem 39:

If p is the perimeter of a right angle triangle with integral length sides,
{a,b,c}, there are exactly three solutions for p = 120.

{20,48,52}, {24,45,51}, {30,40,50}

For which value of p ≤ 1000, is the number of solutions maximised?
'''

def get_solutions(perim):
    #solutions = []
    count = 0
    for hypot in range(3, perim):
        h2 = hypot**2
        for leg1 in range(1, int((perim-hypot)/2)+1):
            leg2 = perim-hypot-leg1
            if h2 == leg1**2 + leg2**2:
                #solutions.append([hypot, leg1, leg2])
                count += 1
    #return solutions
    return count
            

def main(n):
    #n is the maximum perimeter we are considering
    max_sols = 0
    winner = None
    for perim in range(4, n+1):
        #solutions = int(len(get_solutions(perim))/2)
        solutions = get_solutions(perim)
        if solutions > max_sols:
            max_sols = solutions
            winner = perim
    return winner

def build_up(n):
    #n is max
    solutions = {i : 0 for i in range(1, n+1)}
    for hypot in range(4, n+1):
        c2 = hypot**2
        for leg1 in range(1, hypot):
            a2 = leg1**2
            leg2 = (c2 - a2)**0.5
            if int(leg2) == leg2:
                #print(leg1, int(leg2), hypot)
                perim = hypot+leg1+int(leg2)
                if perim <= n:
                    solutions[perim] += 1
##            for leg2 in range(1, n-hypot-leg1+1):
##                #print(hypot, leg1, leg2)
##                b2 = leg2**2
##                if a2 + b2 == c2:
##                    solutions[hypot+leg1+leg2] += 0.5
    #return solutions
    return max(solutions, key=solutions.get)


print("Problem 39 solution: " + str(build_up(1000)))
