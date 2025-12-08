
def read_data(file_path):
    with open(file_path) as f:
        data = f.readlines() 

        lines = []
        for line in data:
            lines.append(line.strip())

        return lines

ex_data = read_data("day7/example.data")
real_data = read_data("day7/real.data")

def part1(map):
    #current_position = (0, map[0].index("S"))
    #print("Starting position ", current_position)

    splits = 0
    lasers = set([map[0].index("S")])

    for layer in map[1:]:
        print(lasers)
        for pos, c in enumerate(layer):
            if c == "^":
                if pos in lasers:
                    splits += 1
                    lasers.remove(pos)
                    lasers.add(pos-1)
                    lasers.add(pos+1)

    print("Result: ", splits)

cache = {}

def move_down(map, x, y):

    print(x,y)
    if (x,y) in cache:
        return cache[(x,y)]

    if y == len(map) - 1:
        return 1

    result = 0
    if map[y + 1][x] == "^":
        result += move_down(map, x - 1, y + 1)
        result += move_down(map, x + 1, y + 1)
    else:
        result += move_down(map, x, y + 1)
    
    cache[(x,y)] = result
    return result


def part2(map):
    print("Result: ", move_down(map, map[0].index("S"), 0))

part2(real_data)