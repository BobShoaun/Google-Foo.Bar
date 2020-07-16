from typing import List

class Node:

    walkable :bool
    x :int
    y: int
    g_cost : int = 0
    h_cost: int = 0

    parent = None

    def __init__(self, walkable, x, y):
        self.walkable = walkable
        self.x = x
        self.y = y
        self.g_cost = 0
        self.h_cost = 0

    def f_cost(self):
        return self.g_cost + self.h_cost


class Grid:

    grid : List[List[Node]] = []
    width = 0
    height = 0
    path : list

    def __init__(self, map):
        self.grid = []
        self.path = []
        for y in range(len(map)):
            row = []
            for x in range(len(map[y])):
                row.append(Node(map[y][x] == 0, x, y))
            self.grid.append(row)

        self.height = len(map)
        self.width = len(map[0])


    def get_neighbours(self, node: Node):
        neighbours = []
        if node.y - 1 >= 0: # top
            neighbours.append(self.grid[node.y - 1][node.x])
        if node.y + 1 < self.height: # bottom
            neighbours.append(self.grid[node.y + 1][node.x])
        if node.x - 1 >= 0: # left
            neighbours.append(self.grid[node.y][node.x - 1])
        if node.x + 1 < self.width: # right
            neighbours.append(self.grid[node.y][node.x + 1])
        return neighbours

    def get_distance(self, nodeA: Node, nodeB : Node):
        return abs(nodeA.x - nodeB.x) + abs(nodeA.y - nodeB.y)


    def find_path(self, start: Node, target: Node):
        openSet = []
        closedSet = []
        openSet.append(start)

        while len(openSet) > 0:
            currentNode = openSet[0]
            for i in range(1, len(openSet)):
                if openSet[i].f_cost() < currentNode.f_cost() or openSet[i].f_cost() == currentNode.f_cost() and openSet[i].h_cost < currentNode.h_cost:
                    currentNode = openSet[i]
            
            openSet.remove(currentNode)
            closedSet.append(currentNode)

            if currentNode == target:
                self.path = self.retrace_path(start, target)
                return

            neighbours = self.get_neighbours(currentNode)
            for i in range(len(neighbours)):
                if not neighbours[i].walkable or neighbours[i] in closedSet:
                    continue

                newMovementCostToNeighbour = currentNode.g_cost + self.get_distance(currentNode, neighbours[i])
                if newMovementCostToNeighbour < neighbours[i].g_cost or neighbours[i] not in openSet:
                    neighbours[i].g_cost = newMovementCostToNeighbour
                    neighbours[i].h_cost = self.get_distance(neighbours[i], target)
                    neighbours[i].parent = currentNode

                    if neighbours[i] not in openSet:
                        openSet.append(neighbours[i])


    def retrace_path(self, start: Node, end: Node):
        path = []
        currentNode = end
        while currentNode != start:
            path.append(currentNode)
            currentNode = currentNode.parent
        
        path.reverse()
        for x in path:
            print(x.x, x.y)
        return path



            
