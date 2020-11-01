import heapq
import math

# returns the number of moves required to solve a maze from start to finish
def solution(map):
    # dimensions of map
    num_rows = len(map)
    num_cols = len(map[0])

    # find the least costly path from start to end
    explore(map, (num_rows-1, num_cols-1))
    smallest_cost = map[0][0]+10    # add 10 to account for the initial move

    # return the number of moves from start to end
    return int(smallest_cost/10)

# uses a greedy algorithm to assign a cost to each move, and find the cheapest path to the end
def explore(graph, source):
    pq = [(0, source)]          # nodes to visit
    processed = set()           # visited nodes
    while pq:
        d, u = heapq.heappop(pq)                                    # process smallest unprocessed node in pq
        if u not in processed:
            r, c = u                                                # coordinates of current node
            # check top neighbor
            if r > 0 and (r-1, c) not in processed:
                graph[r-1][c] = relax(u, (r-1, c), graph)           # relax neighbors d
                heapq.heappush(pq, (graph[r-1][c], (r-1, c)))       # add neighbor to pq
            # check left neighbor
            if c > 0 and (r, c-1) not in processed:
                graph[r][c-1] = relax(u, (r, c-1), graph)
                heapq.heappush(pq, (graph[r][c-1], (r, c-1)))
            # check bottom neighbor
            if r < len(graph)-1 and (r+1, c) not in processed:
                graph[r+1][c] = relax(u, (r+1, c), graph)
                heapq.heappush(pq, (graph[r+1][c], (r+1, c)))
            # check right neighbor
            if c < len(graph[0])-1 and (r, c+1) not in processed:
                graph[r][c+1] = relax(u, (r, c+1), graph)
                heapq.heappush(pq, (graph[r][c+1], (r, c+1)))
            processed.add(u)                                        # add current node to processed

# relaxes the distance to child node via parent node
def relax(u, v, g):
    d = 0
    parent_node = g[u[0]][u[1]]
    child_node = g[v[0]][v[1]]
    # d value for walls is infinite
    if child_node == 1 or math.isinf(child_node):
        d = float('inf')
    # d value is adjusted for child node
    elif child_node >= parent_node + 10 or child_node == 0:
        d = parent_node + 10
    return d



