from pprint import pprint
import re
from typing import NamedTuple, Dict, List
import os

raw_rules1 = """light red bags contain 1 bright white bag, 2 muted yellow bags.
dark orange bags contain 3 bright white bags, 4 muted yellow bags.
bright white bags contain 1 shiny gold bag.
muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.
shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.
dark olive bags contain 3 faded blue bags, 4 dotted black bags.
vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.
faded blue bags contain no other bags.
dotted black bags contain no other bags."""


raw_rules2 = """shiny gold bags contain 2 dark red bags.
dark red bags contain 2 dark orange bags.
dark orange bags contain 2 dark yellow bags.
dark yellow bags contain 2 dark green bags.
dark green bags contain 2 dark blue bags.
dark blue bags contain 2 dark violet bags.
dark violet bags contain no other bags."""


def remove_bags(phrase):
  return phrase[:phrase.index(' bag')]


class Bag(NamedTuple):
  name: str
  children: Dict[str, int]


def count_colours(bags, search='shiny gold', colours=set()):
  """bags = [
    Bag(name='light red', children={'bright white': 1, 'muted yellow': 2}),
    Bag(name='dark orange', children={'bright white': 3, 'muted yellow': 4}),
    Bag(name='bright white', children={'shiny gold': 1}),
    Bag(name='muted yellow', children={'shiny gold': 2, 'faded blue': 9}),
    Bag(name='shiny gold', children={'dark olive': 1, 'vibrant plum': 2}),
    Bag(name='dark olive', children={'faded blue': 3, 'dotted black': 4}),
    Bag(name='vibrant plum', children={'faded blue': 5, 'dotted black': 6}),
    Bag(name='faded blue', children={}),
    Bag(name='dotted black', children={})
  ]"""

  # get parents
  parents = set()
  for bag in bags:
    if search in bag.children:
      parents.add(bag.name)
      colours.add(bag.name)

  # get parents of parents
  for parent in parents:
    count_colours(bags, search=parent)
  
  return len(colours)


def get_name_to_bags(bags):
  return {bag.name: bag for bag in bags}


def count_bags(bags, search='shiny gold'):
  name_to_bags = get_name_to_bags(bags)
  count = 0
  for child, num in name_to_bags[search].children.items():
    count += num + num * count_bags(bags, search=child)
  return count


def parse_rule(rule_line):
  parent, children = rule_line.split(' contain ')
  parent = remove_bags(parent)
  children = children.split(', ')
  children = [remove_bags(c) for c in children]
  d = {}
  for child in children:
    num_index = child.index(' ')
    name = child[num_index:].strip()
    if name == 'other':
      d = {}
      break
    num = int(child[:num_index].strip())
    d[name] = num
  return parent, d


def make_bags(lines):
  rules = lines.split('\n')

  bags: List[Bag] = []

  for rule in rules:
    parent, children = parse_rule(rule)
    b = Bag(parent, children)
    bags.append(b)
  return bags


def part1(lines):
  """How many bag colors can eventually
  contain at least one shiny gold bag?"""
  bags = make_bags(lines)
  colours = count_colours(bags)
  return colours


def part2(lines):
  """How many individual bags are required
  inside your single shiny gold bag?"""
  bags = make_bags(lines)
  colours = count_bags(bags)
  return colours


assert part1(raw_rules1) == 4
assert part2(raw_rules1) == 32
assert part2(raw_rules2) == 126


with open(os.path.basename(__file__).replace('.py', '.txt')) as f:
  lines = f.read().strip()
  print(part1(lines))
  print(part2(lines))
