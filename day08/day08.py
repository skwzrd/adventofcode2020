from pprint import pprint
import re
from typing import NamedTuple, Dict, List
import os
from collections import defaultdict


raw1 = """nop +0
acc +1
jmp +4
acc +3
jmp -3
acc -99
acc +1
jmp -4
acc +6"""


class Action(NamedTuple):
  action: str
  num: int
  hit: bool


def get_action_list(raw):
  lines = raw.strip().split('\n')
  actions = []
  for line in lines:
    action, num = line.strip().split(' ')
    num = int(num)
    actions.append(Action(action, num, False))
  return actions


def part1(actions, raw=True):
  if raw:
    actions = get_action_list(actions)

  index = 0
  acc = 0
  loop = 0
  while True:
    action = actions[index]
    actions[index] = Action(action.action, action.num, True)

    if action.hit and raw:
      print('Part One:', acc)
      return acc

    elif action.action == 'nop':
      index += 1

    elif action.action == 'acc':
      index += 1
      acc += action.num

    elif action.action == 'jmp':
      index += action.num
    
    if index == len(actions):
      print('Part Two:', acc)
      return acc

    loop += 1
    if loop > len(actions):
      return None
    index = index % len(actions)


def part2(raw):
  actions = get_action_list(raw)
  new = actions
  for i, action in enumerate(actions):

    actions = new.copy()
    if action.action == 'acc':
      continue
    if action.action == 'nop':
      actions[i] = Action('jmp', action.num, False)
    if action.action == 'jmp':
      actions[i] = Action('nop', action.num, False)

    res = part1(actions, raw=False)
    if res:
      return res


assert(part1(raw1)) == 5
assert(part2(raw1)) == 8


with open(os.path.basename(__file__).replace('.py', '.txt')) as f:
  lines = f.read()
  part1(lines)
  part2(lines)

