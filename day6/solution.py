
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
        operators = []

        for i, line in enumerate(data):
            line = line.strip()

            if i == len(data) - 1:
                operators = line.split()
            else:
                number_row = []
                found_number = ""
                print("Line: ", line)

                for c in line:
                    if c == " ":
                        if len(found_number) > 0:
                            print("Found number /" + found_number + "/")
                            number_row.append(found_number)
                            found_number = ""
                            continue
                    found_number += c
                number_row.append(found_number)

                
                number_list.append(number_row)
        
        return (number_list, operators)


ex_data = read_data2("day6/example.data")
#real_data = read_data2("day6/real.data")

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
    number_list = problems[0]
    operators = problems[1]

    print("Number list", number_list)
    print("operators", operators)

    totals = [1 if o == "*" else 0 for o in operators]

    for row_number in range(len(number_list[0])):
        
        for x in range(3):
            number = ""
            for col_number in range(len(number_list)):
                number += number_list[col_number][row_number][x]

            #print("Found number ", number)


    for problem_array in number_list:
        for p, problem in enumerate(problem_array):
            operator = operators[p]
            totals[p] = calculate(totals[p], problem, operator)

    print("Totals: ", totals)
    print("Result: ", str(sum(totals)))

part2(ex_data)