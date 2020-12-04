from pprint import pprint
import re
from typing import NamedTuple
import os
from collections import defaultdict


data = """ecl:gry pid:860033327 eyr:2020 hcl:#fffffd
byr:1937 iyr:2017 cid:147 hgt:183cm

iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884
hcl:#cfa07d byr:1929

hcl:#ae17e1 iyr:2013
eyr:2024
ecl:brn pid:760753108 byr:1931
hgt:179cm

hcl:#cfa07d eyr:2025 pid:166559648
iyr:2011 ecl:brn hgt:59in"""

required_fields = [
  "byr",
  "iyr",
  "eyr",
  "hgt",
  "hcl",
  "ecl",
  "pid",
  # "cid"
]

invalid_passports = """eyr:1972 cid:100
hcl:#18171d ecl:amb hgt:170 pid:186cm iyr:2018 byr:1926

iyr:2019
hcl:#602927 eyr:1967 hgt:170cm
ecl:grn pid:012533040 byr:1946

hcl:dab227 iyr:2012
ecl:brn hgt:182cm pid:021572410 eyr:2020 byr:1992 cid:277

hgt:59cm ecl:zzz
eyr:2038 hcl:74454a iyr:2023
pid:3556412378 byr:2007"""

valid_passports = """pid:087499704 hgt:74in ecl:grn iyr:2012 eyr:2030 byr:1980
hcl:#623a2f

eyr:2029 ecl:blu cid:129 byr:1989
iyr:2014 pid:896056539 hcl:#a97842 hgt:165cm

hcl:#888785
hgt:164cm byr:2001 iyr:2015 cid:88
pid:545766238 ecl:hzl
eyr:2022

iyr:2010 hgt:158cm hcl:#b6652a ecl:blu byr:1944 eyr:2021 pid:093154719
"""

def make_dict(info_str):
  """Returns something like
  {
    'byr': '1959',
    'ecl': 'oth',
    'eyr': '2021',
    'hcl': '#c0946f',
    'hgt': '160cm',
    'iyr': '2010',
    'pid': '874577361'
  }
  """
  d={}
  for x in info_str.split():
    k, v = x.split(':')
    k = k.strip()
    v = v.strip()
    d[k] = v
  return d


def validate_int(value, min, max):
  try:
    value = value.strip()
    year = int(value)
    return min <= year <= max
  except:
    return False


def validate_field(key, value):
  value = value.strip()

  if key == 'byr':
    return validate_int( value, 1920, 2002)

  if key == 'iyr':
    return validate_int(value, 2010, 2020)

  if key == 'eyr':
    return validate_int(value, 2020, 2030)

  if key == 'hgt':
    if value.endswith('cm'):
      height = value.replace('cm', '')
      return validate_int(height, 150, 193)

    elif value.endswith('in'):
      height = value.replace('in', '')
      return validate_int(height, 59, 76)
    
    else:
      return False
  
  if key == 'hcl':
    return bool(re.match(r'^#[0-9a-f]{6}$', value))
  
  if key == 'ecl':
    return value in {"amb", "blu", "brn", "gry", "grn", "hzl", "oth"}
  
  if key == 'pid':
    return bool(re.match(r'^[0-9]{9}$', value))
  
  raise ValueError('Should not be here')


assert validate_field('byr', '2002') == True
assert validate_field('byr', '2003') == False
assert validate_field('hgt', '60in') == True
assert validate_field('hgt', '190cm') == True
assert validate_field('hgt', '190in') == False
assert validate_field('hgt', '190') == False
assert validate_field('hcl', '#123abc') == True
assert validate_field('hcl', '#123abz') == False
assert validate_field('hcl', '123abc') == False
assert validate_field('ecl', 'brn') == True
assert validate_field('ecl', 'wat') == False
assert validate_field('pid', '000000001') == True
assert validate_field('pid', '0123456789') == False


def is_valid(passport):
  for field in required_fields:
    if field not in passport.keys():
      return False
    value = passport[field]
    valid = validate_field(field, value)
    # print('field', field, 'value', value, 'valid', valid)
    if not valid:
      return False
  return True


def get_valid_count(data):
  data = data.split('\n')
  index = 0
  raw_passports = defaultdict(list)
  # grouping passport info together using a dict
  for i, info in enumerate(data):
    if info == '':
      index += 1
    if info != '':
      raw_passports[index].append(info)

  # a list of dictionaries containing password key:values
  passports = []
  for key, val in raw_passports.items():
    all_info = ' '.join(val)
    fields = make_dict(all_info)
    passports.append(fields)

  valid_count = 0
  for p in passports:
    if is_valid(p):
      valid_count+=1
  return valid_count

assert get_valid_count(data) == 2
assert get_valid_count(valid_passports) == 4
assert get_valid_count(invalid_passports) == 0

with open(os.path.basename(__file__).replace('.py', '.txt')) as f:
  lines = f.read()
  print(get_valid_count(lines))

