import networkx as nx
import intcode2019 as intc
from collections import defaultdict
from aocd.models import Puzzle
import string


maze_str = Puzzle(year=2019,day=20).input_data.split('\n')
# maze_str = """         A           
#          A           
#   #######.#########  
#   #######.........#  
#   #######.#######.#  
#   #######.#######.#  
#   #######.#######.#  
#   #####  B    ###.#  
# BC...##  C    ###.#  
#   ##.##       ###.#  
#   ##...DE  F  ###.#  
#   #####    G  ###.#  
#   #########.#####.#  
# DE..#######...###.#  
#   #.#########.###.#  
# FG..#########.....#  
#   ###########.#####  
#              Z       
#              Z       """.split('\n')
# print(maze_str)

level = 0
maze = nx.Graph()
maxx = len(maze_str[0])-1
maxy = len(maze_str)-1
start = (1,1,1)
end = (1,1,1)

# Start by adding the letter of . cells
# Letter-to-letter or letter-to-. have 0 weight, while .-. have 1

def build_maze_part1():
  for y in range(len(maze_str)-1):
    row = maze_str[y]
    for x in range(len(row)-1):
      cc = row[x]
      if cc == '.':
        if maze_str[y][x+1] == '.':
          maze.add_edge((x,y),(x+1,y),weight=1)
        if maze_str[y+1][x] == '.':
          maze.add_edge((x,y),(x,y+1),weight=1)
      if cc in string.ascii_uppercase:
        if maze_str[y][x+1] in string.ascii_uppercase:
          if x >= 1 and maze_str[y][x-1] == '.':
            portals[''.join([cc, maze_str[y][x+1]])].append((x-1,y))
          if x+2 < len(row) and maze_str[y][x+2] == '.':
            portals[''.join([cc, maze_str[y][x+1]])].append((x+2,y))  
        if maze_str[y+1][x] in string.ascii_uppercase:
          if y >= 1 and maze_str[y-1][x] == '.':
            portals[''.join([cc, maze_str[y+1][x]])].append((x,y-1))
          if y+2 < len(maze_str) and maze_str[y+2][x] == '.':
            portals[''.join([cc, maze_str[y+1][x]])].append((x,y+2))  
  for portal in portals:
    cells = portals[portal]
    if len(cells) == 2:
      maze.add_edge(cells[0], cells[1], weigth=1)

def build_maze_part2():
  global start
  global end
  portals = defaultdict(list)
  for y in range(len(maze_str)-1):
    row = maze_str[y]
    for x in range(len(row)-1):
      cc = row[x]
      if cc == '.':
        if maze_str[y][x+1] == '.':
          maze.add_edge((x,y,level),(x+1,y,level),weight=1)
        if maze_str[y+1][x] == '.':
          maze.add_edge((x,y,level),(x,y+1,level),weight=1)
      if cc in string.ascii_uppercase:
        if maze_str[y][x+1] in string.ascii_uppercase:
          if x >= 1 and maze_str[y][x-1] == '.':
            portals[''.join([cc, maze_str[y][x+1]])].append((x-1,y,level))
          if x+2 < len(row) and maze_str[y][x+2] == '.':
            portals[''.join([cc, maze_str[y][x+1]])].append((x+2,y,level))  
        if maze_str[y+1][x] in string.ascii_uppercase:
          if y >= 1 and maze_str[y-1][x] == '.':
            portals[''.join([cc, maze_str[y+1][x]])].append((x,y-1,level))
          if y+2 < len(maze_str) and maze_str[y+2][x] == '.':
            portals[''.join([cc, maze_str[y+1][x]])].append((x,y+2,level))  
  for portal in portals:
    cells = portals[portal]
    if len(cells) == 2:
      if cells[0][0] == 2 or cells[0][0] == maxx-2 or cells[0][1] == 2 or cells[0][1] == maxy-2:
        outer = cells[0]
        inner = cells[1]
      else:
        outer = cells[1]
        inner = cells[0]
      maze.add_edge((inner[0], inner[1], level), (outer[0], outer[1], level+1), weigth=1)
    elif level == 0:
      if portal == 'AA':
        start = (cells[0][0], cells[0][1], 0)
      else:
        end = (cells[0][0], cells[0][1], 0)
path_found = False

while not path_found:
  build_maze_part2()
  try:
    print(len(nx.dijkstra_path(maze,start, end))-1)
    path_found = True
  except:
    level = level + 1

    
