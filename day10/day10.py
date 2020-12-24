raw1 = """16
10
15
5
1
11
7
19
6
12
4"""

raw2 = """28
33
18
42
31
14
46
20
48
47
24
23
49
45
19
38
39
11
1
32
25
35
8
17
7
9
4
2
34
10
3"""

def get_adapters(raw):
    return [int(x.strip()) for x in raw.split()]


def part1(adapters):
    one = 0
    three = 1

    adapters.sort()
    if adapters[0] == 1:
        one += 1
    else:
        three += 1

    for i, adapter in enumerate(adapters[:-1]):
        if adapter + 1 == adapters[i+1]:
            one += 1
        else:
            three += 1
    return one * three


assert part1(get_adapters(raw1)) == 35
assert part1(get_adapters(raw2)) == 220


def part2(adapters):
    input_adapter = 0
    output_adapter = max(adapters) + 3

    adapters.append(input_adapter)
    adapters.append(output_adapter)

    arrangements = [0] * (output_adapter + 1)
    arrangements[0] = 1

    if 1 in adapters:
        arrangements[1] = 1

    if 1 in adapters and 2 in adapters:
        arrangements[2] = 2
    elif 2 in adapters:
        arrangements[2] = 1
    
    for n in range(3, output_adapter + 1):
        if n not in adapters:
            continue

        arrangements[n] = arrangements[n-3] + arrangements[n-2] + arrangements[n-1]
    
    return arrangements[output_adapter]

assert(part2(get_adapters(raw1))) == 8
assert(part2(get_adapters(raw2))) == 19208


def main():
    with open('day10.txt') as f:
        raw_adapters = f.read()
    adapters = get_adapters(raw_adapters)
    print(part1(adapters))
    print(part2(adapters))


if __name__ == '__main__':
    main()