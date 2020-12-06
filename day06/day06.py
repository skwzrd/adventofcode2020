from pprint import pprint
import re
from typing import NamedTuple
import os
from collections import defaultdict


raw_data = """abc

a
b
c

ab
ac

a
a
a
a

b"""


def part1(raw_data):
    """For each group, count the number of questions
    to which anyone answered "yes".
    What is the sum of those counts?"""
    groups = raw_data.strip().split('\n\n')

    yes = 0
    for group in groups:
        answers = set(group.replace('\n', ''))
        yes += len(answers)
    return yes

assert part1(raw_data) == 11


def part2(raw_data):
    """For each group, count the number of questions
    to which everyone answered "yes".
    What is the sum of those counts?"""
    groups = raw_data.strip().split('\n\n')

    yes = 0
    for group in groups:
        answers = [set(ans) for ans in group.split('\n')]
        yes += len(set.intersection(*answers))
    return yes


assert part2("abc") == 3
assert part2("\n\nabc\n\n") == 3
assert part2("a\nb\nc") == 0
assert part2("ab\nbc") == 1
assert part2("a\na\na\na") == 1
assert part2("b") == 1
assert part2(raw_data) == 6

with open(os.path.basename(__file__).replace('.py', '.txt')) as f:
  lines = f.read()
  print(part1(lines))
  print(part2(lines))

