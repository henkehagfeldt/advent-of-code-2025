
with open("day2/example.data") as f:
    example_data = f.readlines()

with open("day2/real.data") as f:
    real_data = f.readlines()


def part1(data):
    invalid_ids = []
    ranges = data[0].split(",")
    for r in ranges:
        [start, end] = r.split("-")
        print("start", start, "end", end)
        for i in range(int(start), int(end) + 1):
            number = str(i)
            part = number[0:int(len(number)/2)]
            #print("Checking part ", part, "*2 ", part * 2, " with ", number)
            if part * 2 == number:
                invalid_ids.append(int(number))
        
    print("Invalid ids: ", invalid_ids)
    print("Result: ", str(sum(invalid_ids)))

def part2(data):
    invalid_ids = []
    ranges = data[0].split(",")
    for r in ranges:
        [start, end] = r.split("-")
        #print("start", start, "end", end)
        for i in range(int(start), int(end) + 1):
            number = str(i)
            #print("Number: ", number)
            potential_sequences = [number[:n] for n in range(1, int(len(number) / 2) + 1)]
            #print("Potential: ", potential_sequences)

            for i, pot in enumerate(potential_sequences):
                #print("Checking: ", pot * int(len(number) / (i + 1)), "with", number)
                if pot * int(len(number) / (i + 1)) == number:
                    #print("Sequence found", pot)
                    invalid_ids.append(int(number))
                    break
        
    print("Invalid ids: ", invalid_ids)
    print("Result: ", str(sum(invalid_ids)))

part2(real_data)