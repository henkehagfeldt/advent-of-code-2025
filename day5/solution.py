
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
    combined_ranges = set(ingredients_ranges)

    while True:

        new_combined = set()
        merged_amount = 0

        for r1 in combined_ranges:
            got_merged = False
            for r2 in combined_ranges:
                if r1 != r2:
                    l1, h1 = int(r1.split("-")[0]), int(r1.split("-")[1])
                    l2, h2 = int(r2.split("-")[0]), int(r2.split("-")[1])

                    # R1 covers R2
                    if l1 <= l2 and h1 >= h2:
                        new_combined.add(r1)
                        got_merged = True
                        merged_amount += 1
                        break
                    # R2 covers R1
                    elif l2 <= l1 and h2 >= h1:
                        new_combined.add(r2)
                        got_merged = True
                        merged_amount += 1
                        break
                    # R1 overlaps from left side
                    elif h1 >= l2 and h1 <= h2:
                        new_combined.add(str(l1)+"-"+str(h2))
                        got_merged = True
                        merged_amount += 1
                        break
                    # R1 overlaps from right side
                    elif l1 >= l2 and l1 <= h2:
                        new_combined.add(str(l2)+"-"+str(h1))
                        got_merged = True
                        merged_amount += 1
                        break
            
            if not got_merged:
                new_combined.add(r1)
        
        if merged_amount == 0:
            break

        combined_ranges = new_combined
        
    print("Combined: ", combined_ranges)

    total = 0
    
    for c in combined_ranges:
        low, high = int(c.split("-")[0]), int(c.split("-")[1])
        this_total = high - low + 1
        #print("This total ", this_total)
        total += this_total

    print("Result ", total)
part2(real_ingredients[0])