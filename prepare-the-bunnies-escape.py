
def solution(map):
    height = len(map)
    width = len(map[0])
    optimum = height + width - 1
    steps = 1
    current = [0, 0]

    while current != [height - 1, width - 1]:
        if current[1] + 1 < width and map[current[0]][current[1] + 1] == 0:
            current[1] += 1

        elif current[0] + 1 < height and map[current[0] + 1][current[1]] == 0:
            current[0] += 1

        elif current[1] - 1 >= 0 and map[current[0]][current[1] - 1] == 0:
            current[1] -= 1

        elif current[0] - 1 >= 0 and map[current[0] - 1][current[1]] == 0:
            current[0] -= 1
        print(steps, current)
        map[current[0]][current[1]] = 2
        steps += 1

    return steps


x1 = solution([[0, 1, 1, 0], 
               [0, 0, 0, 1], 
               [1, 1, 0, 0], 
               [1, 1, 1, 0]]) # 4 by 4 grids are always 7

print (x1)
assert x1 == 7

x2 = solution([[0, 0, 0, 0, 0, 0], 
               [1, 1, 1, 1, 1, 0], 
               [0, 0, 0, 0, 0, 0], 
               [0, 1, 1, 1, 1, 1], 
               [0, 1, 1, 1, 1, 1], 
               [0, 0, 0, 0, 0, 0]])
assert x2 == 11

x3 = solution([[0, 0, 0, 0, 0, 0], 
               [1, 1, 1, 1, 1, 0], 
               [1, 1, 1, 0, 0, 0], 
               [1, 1, 0, 0, 1, 1], 
               [1, 1, 0, 1, 1, 1], 
               [1, 1, 0, 0, 0, 0]])
assert x3 == 13

x4 = solution([[0, 0, 0, 1, 0, 0], 
               [1, 0, 1, 1, 1, 0], 
               [1, 0, 1, 0, 0, 0], 
               [1, 0, 0, 0, 1, 1], 
               [1, 1, 0, 1, 1, 1], 
               [1, 1, 0, 0, 0, 0]])
assert x4 == 11


