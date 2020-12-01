
def func(l):
  for i, x in enumerate(l):
    for j, y in enumerate(l[i+1:]):
      if x + y == 2020:
        print("x    y    x*y")
        print(x, y, x*y)
        return x*y

l = [
  1721,
  979,
  366,
  299,
  675,
  1456
]
assert func(l) == 514579

def func2(l):
  for i, x in enumerate(l):
    for j, y in enumerate(l[i+1:]):
      for k, z in enumerate(l[j:]):
        if x + y + z == 2020:
          print(x, y, z, x * y *z)
          return


with open('day01.txt') as f:
  lines = [int(line.strip()) for line in f.readlines()]
  func(lines)
  func2(lines)

