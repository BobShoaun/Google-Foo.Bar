from bunnie import Grid, Node

def solution_old(map):
    
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

def solution_old2(map):
    height = len(map)
    width = len(map[0])
    grid = Grid(map)
    grid.find_path(grid.grid[0][0], grid.grid[height-1][width-1])
    return len(grid.path) + 1

def shortest_path(s_x, s_y, map):
    width = len(map[0])
    height = len(map)
    board = [[None for i in range(width)] for i in range(height)]
    board[s_x][s_y] = 1
    array = [(s_x, s_y)]
    while array:
        x, y = array.pop(0)
        for i in [[1,0],[-1,0],[0,-1],[0,1]]:
          n_x, n_y = x + i[0], y + i[1]
          if 0 <= n_x < height and 0 <= n_y < width:
            if board[n_x][n_y] is None:
                board[n_x][n_y] = board[x][y] + 1
                if map[n_x][n_y] == 1 :
                  continue
                array.append((n_x, n_y)) 
    return board

def solution(map):
    width = len(map[0])
    height = len(map)
    t_b = shortest_path(0, 0, map)
    b_t = shortest_path(height - 1, width - 1, map)
    board = []
    answer = 2 ** 32 - 1
    for i in range(height):
        for j in range(width):
            if t_b[i][j] and b_t[i][j]:
                answer = min(t_b[i][j] + b_t[i][j] - 1, answer)
    return answer


# x1 = solution([[0, 1, 1, 0], 
#                [0, 0, 0, 1], 
#                [1, 1, 0, 0], 
#                [1, 1, 1, 0]]) # 4 by 4 grids are always 7

# print (x1)
# assert x1 == 7

# x2 = solution([[0, 0, 0, 0, 0, 0], 
#                [1, 1, 1, 1, 1, 0], 
#                [0, 0, 0, 0, 0, 0], 
#                [0, 1, 1, 1, 1, 1], 
#                [0, 1, 1, 1, 1, 1], 
#                [0, 0, 0, 0, 0, 0]])
# print (x2)
# assert x2 == 11

# x3 = solution([[0, 0, 0, 0, 0, 0], 
#                [1, 1, 1, 1, 1, 0], 
#                [1, 1, 1, 0, 0, 0], 
#                [1, 1, 0, 0, 1, 1], 
#                [1, 1, 0, 1, 1, 1], 
#                [1, 1, 0, 0, 0, 0]])
# print(x3)
# assert x3 == 13

x4 = solution([[0, 0, 0, 1, 0, 0], 
               [1, 0, 1, 1, 1, 0], 
               [1, 0, 1, 0, 0, 0], 
               [1, 0, 0, 0, 1, 1], 
               [1, 1, 0, 1, 1, 1], 
               [1, 1, 0, 0, 0, 0]])
print (x4)
assert x4 == 11


