
with open("day4/example.data") as f:
    example_data = f.readlines()
    matrix_example = []
    for line in example_data:
        row = []
        for c in line.strip():
            row.append(c)
        matrix_example.append(row)

with open("day4/real.data") as f:
    example_data = f.readlines()
    matrix_real = []
    for line in example_data:
        row = []
        for c in line.strip():
            row.append(c)
        matrix_real.append(row)


def part1(matrix):
    result = 0
    for y in range(len(matrix)):
        for x in range(len(matrix[0])):

            if matrix[y][x] == "@":
                rolls = checkAround(x, y, matrix)

                if rolls < 4:
                    result += 1
                    print("Roll y", y, "x", x)

    print("Result: ", result)




def checkAround(x, y, matrix):
    rolls = 0
    if y == 0:
        if x == 0:
            rolls += check(matrix[y+1][x])
            rolls += check(matrix[y+1][x+1])
            rolls += check(matrix[y][x+1])
        elif x == len(matrix[0]) - 1:
            rolls += check(matrix[y+1][x])
            rolls += check(matrix[y+1][x-1])
            rolls += check(matrix[y][x-1])
        else:
            rolls += check(matrix[y+1][x])
            rolls += check(matrix[y+1][x+1])
            rolls += check(matrix[y][x+1])
            rolls += check(matrix[y+1][x-1])
            rolls += check(matrix[y][x-1])
    elif y == len(matrix) - 1:
        if x == 0:
            rolls += check(matrix[y-1][x])
            rolls += check(matrix[y-1][x+1])
            rolls += check(matrix[y][x+1])
        elif x == len(matrix[0]) - 1:
            rolls += check(matrix[y-1][x])
            rolls += check(matrix[y-1][x-1])
            rolls += check(matrix[y][x-1])
        else:
            rolls += check(matrix[y-1][x+1])
            rolls += check(matrix[y][x+1])
            rolls += check(matrix[y-1][x])
            rolls += check(matrix[y-1][x-1])
            rolls += check(matrix[y][x-1])
    else:
        if x == 0:
            rolls += check(matrix[y-1][x])
            rolls += check(matrix[y-1][x+1])
            rolls += check(matrix[y][x+1])
            rolls += check(matrix[y+1][x])
            rolls += check(matrix[y+1][x+1])
        elif x == len(matrix[0]) - 1:
            rolls += check(matrix[y-1][x])
            rolls += check(matrix[y-1][x-1])
            rolls += check(matrix[y][x-1])
            rolls += check(matrix[y+1][x])
            rolls += check(matrix[y+1][x-1])
        else:
            rolls += check(matrix[y][x-1])
            rolls += check(matrix[y][x+1])
            rolls += check(matrix[y-1][x-1])
            rolls += check(matrix[y-1][x])
            rolls += check(matrix[y-1][x+1])
            rolls += check(matrix[y+1][x-1])            
            rolls += check(matrix[y+1][x])
            rolls += check(matrix[y+1][x+1])
    return rolls

def check(character):
    return int(character == "@")

def part2(matrix):
    result = 0
    while True:
        (found_rolls, matrix) = checkAll(matrix)

        if found_rolls == 0:
            break
        else:
            result += found_rolls
    
    print("Result", result)

def checkAll(matrix):
    result = 0
    new_matrix = []
    for y in range(len(matrix)):
        new_row = []
        for x in range(len(matrix[0])):

            if matrix[y][x] == "@":
                rolls = checkAround(x, y, matrix)

                if rolls < 4:
                    result += 1
                    new_row.append(".")
                else:
                    new_row.append("@")
            else:
                new_row.append(".")
        new_matrix.append(new_row)

    return (result, new_matrix)

part2(matrix_real)