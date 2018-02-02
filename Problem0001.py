'''
Project Euler problem 1:

If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
'''

def get_multiples_of_x_below_y(x, y):
    multiples = set()
    for i in range(1, y):
        if i % x == 0:
            multiples.add(i)
    return multiples

def get_multiples_of_k_and_l_below_m(k, l, m):
    mult_of_k = get_multiples_of_x_below_y(k, m)
    mult_of_l = get_multiples_of_x_below_y(l, m)
    all_multiples = mult_of_k.union(mult_of_l)
    result_sum = 0
    for item in all_multiples:
        result_sum += item
    return result_sum
    
print("Problem 1 solution: " + str(get_multiples_of_k_and_l_below_m(3, 5, 1000)))

