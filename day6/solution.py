
def read_data(file_path):
    with open(file_path) as f:
        data = f.readlines() 
        number_list = []
        operators = []

        for i, line in enumerate(data):
            line = line.strip()

            if i == len(data) - 1:
                operators = line.split()
            else:
                number_row = []
                for number in line.split():
                    number_row.append(int(number))
                
                number_list.append(number_row)
        
        return (number_list, operators)

def read_data2(file_path):
    with open(file_path) as f:
        data = f.readlines() 
        number_list = []

        operators_line = data[len(data) - 1]
        operators = []
        for i, o in enumerate(operators_line.strip()):
            if o != " ":
                operators.append((i, o))

        for o in range(len(operators)):
            o_index = operators[o][0]
            next_o_index = len(data[0]) if o == len(operators) - 1 else operators[o+1][0]

            column = []
            for y in range(len(data) - 1):
                value = ""
                for x in range(o_index, next_o_index-1):
                    value += data[y][x].strip("\n")
                print("Value: ", value)
                column.append(value)
            print("Column: ", column)
            number_list.append(column)
        
        return number_list, operators


ex_data = read_data2("day6/example.data")
real_data = read_data2("day6/real.data")

def part1(problems):

    number_list = problems[0]
    operators = problems[1]

    print("Number list", number_list)
    print("operators", operators)

    totals = [1 if o == "*" else 0 for o in operators]

    for problem_array in number_list:
        for p, problem in enumerate(problem_array):
            operator = operators[p]
            totals[p] = calculate(totals[p], problem, operator)

    print("Totals: ", totals)
    print("Result: ", str(sum(totals)))


def calculate(total, problem, operator):
    if operator == "*":
        return total * problem
    elif operator == "+":
        return total + problem


def part2(problems):

    print("Number list", problems)

    number_list = problems[0]
    operators = problems[1]

    totals = 0

    for c, column in enumerate(number_list):
        print("Column: ", column)
        operator = operators[c][1]

        numbers = []
        for x in range(len(column[0])-1, -1, -1):
            print(x)
            current_number = ""            
            for y in range(len(column)):
                current_number += column[y][x]
            numbers.append(int(current_number))
        
        print("Numbers: ", numbers)
        print("Operator: ", operator)
        col_total = 1 if operator == "*" else 0

        for number in numbers:
            print(col_total, number, operator)
            if number != None:
                col_total = calculate(col_total, number, operator)
        print("Col total: ", col_total)
        totals += col_total

    print("Result: ", totals)


part2(real_data)