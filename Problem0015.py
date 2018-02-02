'''
Project Euler Problem 15:

Starting in the top left corner of a 2×2 grid, and only being able to
move to the right and down, there are exactly 6 routes to the bottom
right corner.

How many such routes are there through a 20×20 grid?
'''

##def step(path, n):
##    next_steps = []
##    pos = path[-1]
##    if pos[0] == n and pos[1] == n:
##        return path
##    if pos[0] < n:
##        next_step = path + [(pos[0]+1, pos[1])]
##        next_steps.append(next_step)
##    if pos[1] < n:
##        next_step = path + [(pos[0], pos[1]+1)]
##        next_steps.append(next_step)
##    return next_steps
##
##def check_end(paths, n):
##    for path in paths:
##        if path[-1][0] < n or path[-1][1] < n:
##            return True
##    return False
##
##def march(n):
##    paths = [[(0,0)]]
##    while check_end(paths, n):
##        new_paths = []
##        for path in paths:
##            steps = step(path, n)
##            for new_path in steps:
##                new_paths.append(new_path)
##        paths = new_paths
##    #return paths
##    return len(paths)

##def step(pos, n):
##    #if pos[0] == n and pos[1] == n:
##    #    return []
##    steps = []
##    if pos[0] < n:
##        steps.append((pos[0]+1, pos[1]))
##    if pos[1] < n:
##        steps.append((pos[0], pos[1]+1))
##    return steps
##
##def check_positions(positions, n):
##    for pos in positions:
##        if pos[0] < n or pos[1] < n:
##            return True
##    return False
##
##import collections
##
##def count_steps(n):
##    positions = collections.deque()
##    positions.append((0,0))
##    count = 0
##    while len(positions) > 0:
##        pos = positions.pop()
##        steps = step(pos, n)
##        if steps == []:
##            count += 1
##        else:
##            for p in steps:
##                positions.append(p)
##    return count
            
##        new_positions = []
##        for pos in positions:
##            new_steps = step(pos, n)
##            if new_steps is None:
##                count += 1
##            else:
##                for new_step in new_steps:
##                    new_positions.append(new_step)
##        positions = new_positions
##    return count

def backwards(n):
    d = {(n, n) : 1}
    cur_set = [(n, n)]
    while len(cur_set) > 0:
        cur_point = cur_set.pop(0)
        if cur_point[0] != 0:
            above_point = (cur_point[0]-1, cur_point[1])
            if above_point not in cur_set:
                cur_set.append(above_point)
        if cur_point[1] != 0:
            left_point = (cur_point[0], cur_point[1]-1)
            if left_point not in cur_set:
                cur_set.append(left_point)
        score = 0
        #compute score as the sum of the scores of right point and below point
        if cur_point not in d:
            if cur_point[0] != n:
                below_point = (cur_point[0]+1, cur_point[1])
                score += d[below_point]
            if cur_point[1] != n:
                right_point = (cur_point[0], cur_point[1]+1)
                score += d[right_point]
            d[cur_point] = score
    #print(d)
    return d[(0,0)]


print("Problem 15 solution: " + str(backwards(20)))
