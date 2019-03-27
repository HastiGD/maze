class Maze:
    def __init__(self, fname):
        self.read_maze_file(fname)
    
    def read_maze_file(self, fname):
        try:
            fd = open(fname, "r")
            linenum = 1
            vals = [int(x) for x in fd.readline().split()]
            self.dims = (vals[0], vals[1])
            self.start = (vals[2], vals[3])
            self.end = (vals[4], vals[5])
            linenum += 1
            fd.readline()    # discard top wall
            self.right_walls = []
            self.bottom_walls = []
            for r in range(self.dims[0]):
                # process side walls
                self.right_walls.append([])
                linenum += 1
                s = fd.readline()[2::2]
                for c in range(self.dims[1]):
                    self.right_walls[r].append(s[c] == '|')
                # process bottom walls
                self.bottom_walls.append([])
                linenum += 1
                s = fd.readline()[1::2]
                for c in range(self.dims[1]):
                    self.bottom_walls[r].append(s[c] == '-')
        except FileNotFoundError as err:
            raise  # re-raise exception
        except Exception as err:
            print("Processing line", linunum, "raised exception:", err)
            raise  # re-raise exception
    
    def getSize(self):
        return self.dims
    
    def getStart(self):
        return self.start
    
    def getEnd(self):
        return self.end


    def openDirs(self, r, c):
        Dirs = []
        last_row = self.dims[0]-1
        last_col = self.dims[1]-1
        #print("Last column is",last_col)
        #print("Last row is", last_row)
        
        # if we are not at the right edge of the maze, then checks for a right wall
        if c != last_col:
            if not self.right_walls[r][c]:
                #print("There is no right wall where you are")
                Dirs.append("R")

        # if we are not at the left edge of the maze, then checks for a left wall
        if c != 0:
            if not self.right_walls[r][c-1]:
                #print("There is no left wall where you are")
                Dirs.append("L")

        # if we are not at the bottom edge of the maze, then checks for a bottom wall
        if r != last_row:
            if not self.bottom_walls[r][c]:
                #print("There is no bottom wall where you are")
                Dirs.append("D")

        # if we are not at the top edge of the maze, then checks for an upper wall
        if r != 0:
            if not self.bottom_walls[r-1][c]:
                #print("There is no upper wall where you are")
                Dirs.append("U")

        return Dirs
