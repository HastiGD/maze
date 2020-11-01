# returns the number of moves required to solve a maze from start to finish
def solution(map):
    source = (len(map)-1, len(map[0])-1)     # starting position

    # change value of end node to 'E'
    map[0][0] = 'E'

    # call the helper function to explore the map
    explore(map, source)

    # count the number of moves required
    moves = 1
    for row in range(len(map)):
        for col in range(len(map[0])):
            if map[row][col] == 'V':
                moves += 1
    return moves

# solves a maze recursively
def explore(map, node):

    row = node[0]
    col = node[1]

    # check if current node is the end
    if map[row][col] == 'E':
        return True

    # check if current node is a wall
    elif map[row][col] == 1:
        return False

    # check if current node has been visited
    elif map[row][col] == 'V':
        return False

    # if none of the above conditions are met visit current node
    map[row][col] = 'V'

    # explore each neighbor
    top = (row-1, col)
    left = (row, col-1)
    bottom = (row+1, col)
    right = (row, col+1)

    # if any of the neighbors returns True, the solution exists
    if (row > 0 and explore(map, top) or col > 0 and explore(map, left) or row < len(map)-1 and explore(map, bottom) or col < len(map[0])-1 and explore(map, right)):
        return True

    return False
