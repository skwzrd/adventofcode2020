from pprint import pprint
import os

raw1 = """35
20
15
25
47
40
62
55
65
95
102
117
150
182
127
219
299
277
309
576"""


def part1(nums, preamble=25):
  body = nums[preamble:]
  
  for t, target in enumerate(body):
    
    window = nums[t:preamble + t]

    found = False
    for i, h1 in enumerate(window[:-1]):
      for h2 in window[i+1:]:
        if h1 != h2 and h1 + h2 == target:
          found = True
    if not found:
      print("PART ONE:", target)
      return target


def part2(nums, target):
  for n, num in enumerate(nums[:-1]):
    contiguous = [num]
    for w, window_num in enumerate(nums[n+1:]):
      contiguous.append(window_num)
      total = sum(contiguous)
      if total == target:
        print("PART TWO:", min(contiguous) + max(contiguous))
        return min(contiguous) + max(contiguous)


def get_nums(raw):
  return [int(x) for x in raw.split('\n')]


NUMS = get_nums(raw1)
assert(part1(NUMS, preamble=5)) == 127
assert(part2(NUMS, 127)) == 62


with open(os.path.basename(__file__).replace('.py', '.txt')) as f:
  raw = f.read().strip()
  nums = get_nums(raw)
  target = part1(nums)
  part2(nums, target)