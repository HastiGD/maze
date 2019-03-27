import Maze

def solve_maze(r, c, end, visited_lists):
    # r = current row
    # c = current column
    #visited_lists =[] initialization in main()
    
    if (r, c) == end:
        return True
    # add a list of cells already visited
    

    for i in Dirs:
        if i == 'R':
            solve_maze(r, c+1, end)

        if i == 'L':
            solve_maze(r, c-1, end)

        if i == 'U':
            solve_maze(r-1, c, end)

        if i == 'D':
            solve_maze(r+1, c, end)
