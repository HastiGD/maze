#maze solvers
In this project I employ two different methods to solve a maze, recursion and Dijkstra's algorithm. The maze input is given as a list of lists as such:

     0 1 2 3 4
    
0   [0 0 0 0 0]
1   [1 0 1 1 1]
2   [1 0 1 1 1]
3   [1 0 0 0 1]
4   [1 1 1 0 0] <-- start

The start is always at maze[n][n], and the end is always at maze[0][0], a 1 represents a wall which cannot be crossed.
The maze can only be traversed in lateral or horizontal directions. Diagonal travel is not permitted.
The resursive solution searches all possible routes in the maze, and returns as soon as the end reached. The recursive algorithm produces the following solution:

     0 1 2 3 4
    
0   [E V 0 0 0]
1   [1 V 1 1 1]
2   [1 V 1 1 1]
3   [1 V V V 1]
4   [1 1 1 V V]

Each 'V' (visited) cell is summed up, including the 'E' (ending) cell, and the sum represents the total number of moves required to solve the maze. 

The greedy algorithm treats each cell as a node in a graph, assigns a cost of 10 to each move, and returns the shortest path. 
Moving to a wall costs infinity in the greedy algorith to prevent crossing walls. 
The greedy algorithm produces the following solution:

     0   1   2    3   4   5

0   [80,  70,  80,  90,  100]
1   [inf, 60,  inf, inf, inf]
2   [inf, 50,  inf, inf, inf]
3   [inf, 40,  30,  20,  inf]
4   [inf, inf, inf, 10,   0]

The value of maze[0][0]/10 + 1 represents the number of moves from start to end. 

In the recursive solution we search each cell once, resulting in a time complexity of O(V) where V = number of cells. The time complexity of Dijkstra's algorithm is O(ElogV), where each cell shares an edge with up to 4 neighbors. The greedy algorithm is therefore the most efficient algorithm.
