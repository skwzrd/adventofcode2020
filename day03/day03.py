from pprint import pprint
import re
from typing import NamedTuple
import os

def part1(lines):
  trees = 0
  x = 0
  y = 0
  for i, line in enumerate(lines):
    x = (x + 3) % len(line)
    y = y + 1
    if y == len(lines):
      break
    if lines[y][x] == '#':
      trees += 1
  return trees

def part2(lines):
  def _part2(right, down):
    trees = 0
    x = 0
    y = 0
    for i, line in enumerate(lines):
      x = (x + right) % len(line)
      y = y + down
      if y >= len(lines):
        break
      if lines[y][x] == '#':
        trees += 1
    return trees
  
  # (right, down)
  slopes = [(1,1), (3,1), (5,1), (7,1), (1,2)]
  prod = 1
  for slope in slopes:
    prod = prod * _part2(*slope)
  return prod


l = [
  "..##.......",
  "#...#...#..",
  ".#....#..#.",
  "..#.#...#.#",
  ".#...##..#.",
  "..#.##.....",
  ".#.#.#....#",
  ".#........#",
  "#.##...#...",
  "#...##....#",
  ".#..#...#.#",
]
assert part1(l) == 7
assert part2(l) == 336


with open(os.path.basename(__file__).replace('.py', '.txt')) as f:
  lines = [line.strip() for line in f.readlines()]
  print(part1(lines))
  print(part2(lines))
  

