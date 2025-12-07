
with open("day5/example.data") as f:
    example_data = f.readlines()
    example_ingredients = ([], [])
    for line in example_data:
        line = line.strip()
        if "-" in line:
            example_ingredients[0].append(line)
        elif len(line) > 0:
            #print(line)
            example_ingredients[1].append(line)

with open("day5/real.data") as f:
    real_data = f.readlines()
    real_ingredients = ([], [])
    for line in real_data:
        line = line.strip()
        if "-" in line:
            real_ingredients[0].append(line)
        elif len(line) > 0:
            #print(line)
            real_ingredients[1].append(line)


def part1(ingredients_ranges, ingredient_ids):
    fresh = 0
    for ingredient in ingredient_ids:
        ingredient = int(ingredient)
        for r in ingredients_ranges:
            low = int(r.split("-")[0])
            high = int(r.split("-")[1])
            if ingredient >= low and ingredient <= high:
                print("Ingredient: ", ingredient, "in range: ", low, " - ", high)
                fresh += 1
                break
    print("Result: ", fresh)

def part2(ingredients_ranges):

    combined_ranges = ingredients_ranges

    while True:
        new_ranges = []
        merged_indices = []

        print("Start: ", combined_ranges)

        for i1, r1 in enumerate(combined_ranges):
            got_merged = False
            for i2, r2 in enumerate(combined_ranges):

                if i1 in merged_indices or i2 in merged_indices or i1 == i2:
                    continue

                l1, h1 = int(r1.split("-")[0]), int(r1.split("-")[1])
                l2, h2 = int(r2.split("-")[0]), int(r2.split("-")[1])

                print(l1, h1, l2, h2)
                if l1 <= l2 and h1 >= h2:
                    print("ONE")
                    new_ranges.append(str(l1) + "-" + str(h1))
                    merged_indices.append(i1)
                    merged_indices.append(i2)
                    got_merged = True
                elif l2 <= l1 and h2 >= h1:
                    print("TWO")
                    new_ranges.append(str(l2) + "-" + str(h2))
                    merged_indices.append(i1)
                    merged_indices.append(i2)
                    got_merged = True
                elif l1 <= l2 and h1 >= l2 and h1 <= h2:
                    print("THREE")
                    new_ranges.append(str(l1) + "-" + str(h2))
                    print("Added: ", new_ranges[len(new_ranges)-1])
                    merged_indices.append(i1)
                    merged_indices.append(i2)
                    got_merged = True
                elif l2 <= l1 and h2 >= l1 and h2 <= h1:
                    print("FOUR")
                    new_ranges.append(str(l2) + "-" + str(h1))
                    merged_indices.append(i1)
                    merged_indices.append(i2)
                    got_merged = True
            if not got_merged:
                new_ranges.append(str(l1) + "-" + str(h1))
                merged_indices.append(i1)
        print("End: ", new_ranges)
        print("Merged: ", merged_indices)

        if len(merged_indices) == 0:
            break
        else:
            combined_ranges = new_ranges
                
    print(combined_ranges)

    total = 0
    for c in combined_ranges:
        low, high = int(c.split("-")[0]), int(c.split("-")[1])
        this_total = high - low + 1
        #print("This total ", this_total)
        total += high - low + 1

    print("Result ", total)
part2(example_ingredients[0])