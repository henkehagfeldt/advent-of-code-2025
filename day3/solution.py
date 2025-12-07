
with open("day3/example.data") as f:
    example_data = f.readlines()

with open("day3/real.data") as f:
    real_data = f.readlines()


def part1(data):

    joltages = []
    for bank in data:
        bank = bank.strip()
        max_number = (0, 0)
        for i, number in enumerate(bank[:-1]):
            number = number.strip()
            if int(number) > int(max_number[1]):
                max_number = (i, number)
        
        second_max = (0, 0)
        for i, number in enumerate(bank[max_number[0] + 1:]):
            number = number.strip()
            if int(number) > int(second_max[1]):
                second_max = (i, number)
        joltages.append(int(max_number[1] + second_max[1]))
        print("Found joltage: ", joltages[-1])

    print("Joltages: ", joltages)
    print("Result: ", str(sum(joltages)))
    
def part2(data):
    joltages = []
    for bank in data:
        bank = bank.strip()
        start = 0
        joltage = ""
        for j in range(12):
            right_most = 11 - j
            max_number = (0, 0)
            if (right_most > 0):
                new_range = bank[start:-right_most]
            else:
                new_range = bank[start:]
            for i, number in enumerate(new_range):
                number = number.strip()
                if int(number) > int(max_number[1]):
                    max_number = (i, number)
            joltage += max_number[1]
            start += max_number[0] + 1

        joltages.append(int(joltage))
        print("Found joltage: ", joltages[-1])

    print("Joltages: ", joltages)
    print("Result: ", str(sum(joltages)))

part2(real_data)