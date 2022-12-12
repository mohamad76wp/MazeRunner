from colorama import init, Fore
import random

wall = 'w'
cell = 'c'

width = 27
height = 11
def init_maze(width, height): # in method bar asas meqdare Variable haye width va height maze tolid mikone
    maze = []
    for i in range(0, height):
        line = []
        for i in range(0, width):
            line.append('u')
        maze.append(line)
    return maze


def print_maze(maze): # in method Maze ke method init_maze tolid mikone ro rangi print mikone
    for i in range(0, len(maze)):
        for j in range(0, len(maze[0])):
            if maze[i][j] == 'u':
                print(Fore.WHITE, f'{maze[i][j]}', end="")
            elif maze[i][j] == 'c':
                print(Fore.GREEN, f'{maze[i][j]}', end="")
            else:
                print(Fore.RED, f'{maze[i][j]}', end="")
        print('\n')


maze_init = init_maze(width, height)

# printmaze = print_maze(maze_init)


# in ja besorat random ye noqte shoro baraye ijad masir maze tolid mikone
starting_height = int(random.random()*height)
starting_width = int(random.random()*width)


# inja check mishe ke on noqte randome tolid shode roye divar haye asli maze nabashe age bod ye block ja be ja mikone ono
if starting_height == 0:
    starting_height += 1
if starting_height == height-1:
    starting_height -= 1
if starting_width == 0:
    starting_width += 1
if starting_width == width-1:
    starting_width -= 1

# inja on noqte start random ro to list maze_init az 'u' be 'c' avaz mikone 
maze_init[starting_height][starting_width] = cell


walls = []
walls.append([starting_height-1, starting_width])
walls.append([starting_height, starting_width-1])
walls.append([starting_height, starting_width+1])
walls.append([starting_height+1, starting_width])

# hamchenin 4 block up down left right noqted start o az 'u' be 'w' taqir mide
maze_init[starting_height-1][starting_width] = wall
maze_init[starting_height][starting_width-1] = wall
maze_init[starting_height][starting_width+1] = wall
maze_init[starting_height+1][starting_width] = wall


# in method miad 4 jahat wall samte raste starting point ra check mikonad va 1 ra return mikonad
# dar asl moshakash mikonad atrafe wall chand block c vojod darad

def surroundingCells(rand_wall): # check how many 4 side of block is c 
    s_cells = 0
    if (maze_init[rand_wall[0]-1][rand_wall[1]] == 'c'): # block up is "c"
        s_cells += 1
    if (maze_init[rand_wall[0]+1][rand_wall[1]] == 'c'): # block down is "c"
        s_cells += 1
    if (maze_init[rand_wall[0]][rand_wall[1]-1] == 'c'): # block right is "c"
        s_cells +=1
    if (maze_init[rand_wall[0]][rand_wall[1]+1] == 'c'): # block left is "C"
        s_cells += 1    
    return s_cells

def delete_wall(rand_wall):
    for wall in walls:
        if (wall[0] == rand_wall[0] and wall[1] == rand_wall[1]):
            walls.remove(wall)  

while walls:
    rand_wall = walls[int(random.random()*len(walls))-1]

    if rand_wall[1] != 0:
        if maze_init[rand_wall[0]][rand_wall[1]-1] == 'u' and maze_init[rand_wall[0]][rand_wall[1]+1] == 'c': #check left is 'u' and right is 'c' of block
            print("case 1")
            s_cells = surroundingCells(rand_wall)
            if s_cells < 2:
                maze_init[rand_wall[0]][rand_wall[1]] = cell
                if (rand_wall[0] != 0):
                    if (maze_init[rand_wall[0]-1][rand_wall[1]] != 'c'):
                        maze_init[rand_wall[0]-1][rand_wall[1]] = wall
                    if ([rand_wall[0]-1, rand_wall[1]] not in walls):
                        walls.append([rand_wall[0]-1, rand_wall[1]])
            delete_wall(rand_wall)
            continue
        continue


    if rand_wall[0] != 0:   
        if maze_init[rand_wall[0]-1][rand_wall[1]] == 'u' and maze_init[rand_wall[0]+1][rand_wall[1]+1] == 'c': # check up is "u" and down-right is "c"
            print("case 2")

    if rand_wall[0] != height-1:
        if maze_init[rand_wall[0]+1][rand_wall[1]] == 'u' and maze_init[rand_wall[0]-1][rand_wall[1]] == 'c': # check down is "u" and up is "C"
            print("case 3")

    if rand_wall[1] != width-1:
        if maze_init[rand_wall[0]][rand_wall[1]+1] == 'u' and maze_init[rand_wall[0]][rand_wall[1]-1] == 'c': # check down is "u" and left is "C"
            print("case 4")

    

