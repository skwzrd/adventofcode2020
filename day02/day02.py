from pprint import pprint as print
from time import time
from functools import wraps
import re
from typing import NamedTuple

def timeit(func):
  @wraps(func)
  def wrapper(*args, **kwargs):
    start = time()
    result = func(*args, **kwargs)
    print(func.__name__ + " " + str(round(time() - start, 3)) + ' seconds.')
    return result
  return wrapper


class Policy(NamedTuple):
  lo: int
  hi: int
  letter: str
  psswd: str

  @staticmethod
  def parse_line(line):
    m = re.match(r'(\d+)-(\d+) (\w): (\w+)', line)
    lo = int(m.groups()[0])
    hi = int(m.groups()[1])
    letter = m.groups()[2]
    psswd = m.groups()[3]

    return Policy(lo, hi, letter, psswd)


  def is_valid1(self):
    counts = self.psswd.count(self.letter)
    return (counts >= self.lo) and (counts <= self.hi)


  def is_valid2(self):
    match_count = 0
    if(self.psswd[self.lo - 1] == self.letter):
      match_count += 1

    if(self.psswd[self.hi - 1] == self.letter):
      match_count += 1

    return match_count == 1


@timeit
def part1(lines):
  total = sum([Policy.parse_line(line).is_valid1() for line in lines])
  return total

@timeit
def part2(lines):
  total = sum([Policy.parse_line(line).is_valid2() for line in lines])
  return total

l = [
  "1-3 a: abcde",
  "1-3 b: cdefg",
  "2-9 c: ccccccccc"
]
assert part1(l) == 2
assert part2(l) == 1


with open('day02.txt') as f:
  lines = [line.strip() for line in f.readlines()]
  print(part1(lines))
  print(part2(lines))
  

