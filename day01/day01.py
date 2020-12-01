
SUM = 2020

def part1(l):
  diffs = {SUM - i for i in l}
  for x in diffs:
    if x in l:
      return (SUM - x) * x

l = [
  1721,
  979,
  366,
  299,
  675,
  1456
]

assert part1(l) == 514579


def part2(l):
  diffs = { 
            SUM - i - j: (i, j)
            for i in l
            for j in l
          }
  for x in l:
    if x in diffs:
      i, j = diffs[x]
      return i * j * x


with open('day01.txt') as f:
  lines = [int(line.strip()) for line in f.readlines()]
  assert part1(lines) == 1006875
  assert part2(lines) == 165026160

