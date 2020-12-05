import os

def get_row(seat):
  seat = seat[:7]
  hi = 127
  lo = 0
  for r in seat:
    mid = int((hi - lo) / 2)
    
    if r == 'F':
      hi = mid + lo
    if r == 'B':
      lo += mid + 1
  
  if seat[-1] == 'F':
    return lo
  return hi


def get_col(seat):
  seat = seat[7:]
  hi = 7
  cols = list(range(hi+1))
  for c in seat:
    mid = int(len(cols)/2)
    if c == 'R':
      cols = cols[mid:]
    else:
      cols = cols[:mid]
  return cols[0]


def get_seat_id(seat):
  row = get_row(seat)
  col = get_col(seat)
  return row * 8 + col


assert get_row('FBFBBFFRLR') == 44
assert get_col('FBFBBFFRLR') == 5
assert get_seat_id('FBFBBFFRLR') == 357

assert get_row('BFFFBBFRRR') == 70
assert get_col('BFFFBBFRRR') == 7
assert get_seat_id('BFFFBBFRRR') == 567

assert get_row('FFFBBBFRRR') == 14
assert get_col('FFFBBBFRRR') == 7
assert get_seat_id('FFFBBBFRRR') == 119

assert get_row('BBFFBBFRLL') == 102
assert get_col('BBFFBBFRLL') == 4
assert get_seat_id('BBFFBBFRLL') == 820


with open(os.path.basename(__file__).replace('.py', '.txt')) as f:
  lines = [line.strip() for line in f]
  seat_ids = [get_seat_id(line) for line in lines]

  # part 1
  max_seat_id = max(seat_ids)
  print(max_seat_id) # 801

  # part 2
  seat_ids.sort()
  for i, seat_id in enumerate(seat_ids[:-1]):
    if seat_id + 1 != seat_ids[i+1]:
      print(seat_id + 1) # 597
