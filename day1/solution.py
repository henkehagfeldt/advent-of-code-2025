
with open("day1/example.data") as f:
    example_states = f.readlines()

with open("day1/real.data") as f:
    real_states = f.readlines()


def part1(states):
    dial_state = 50
    password = 0

    for state in states:
        number = int(state[1:])
        if state[0] == "L":
            dial_state = (dial_state - number) % 100
        else:
            dial_state = (dial_state + number) % 100
        
        password += int(dial_state == 0)
        

    print(password)


def part2(states):
    dial_state = 50
    password = 0

    for s, state in enumerate(states):
        number = int(state[1:])
        old_state = str(dial_state)
        passes = 0

        if state[0] == "L":
            new_dial_state = dial_state - number
            passes = (dial_state // 100) - ((new_dial_state - 1) // 100)
        
        else:
            new_dial_state = dial_state + number
            passes = new_dial_state // 100 - dial_state // 100
        
        password += passes
        dial_state = new_dial_state

    print(dial_state)
    print(password)

def part2s(states):
    dial_state = 50
    password = 0

    for s, state in enumerate(states):
        old_state = str(dial_state)
        for i in range(int(state[1:])):
            if state[0] == "L":
                dial_state = (dial_state - 1) % 100
            else:
                dial_state = (dial_state + 1) % 100

            if dial_state == 0:
                password += 1

                #print(old_state + "->" + state, end="")

    print(dial_state)
    print(password)

def part2_fixed(states):
    # Track the absolute position (infinite number line)
    # Start at 50
    abs_state = 50 
    password = 0

    for state in states:
        number = int(state[1:])
        direction = state[0]
        
        # Determine the new absolute position based on direction
        if direction == "R":
            new_abs_state = abs_state + number
            
            # Formula: How many 100s boundaries exist between start and end?
            # For Right, we just need integer division
            passes = (new_abs_state // 100) - (abs_state // 100)
            
        else: # "L"
            new_abs_state = abs_state - number
            
            # For Left, we want to count hitting 0 as well.
            # We treat the boundary as inclusive on the top end for subtraction logic.
            # Logic: (Start // 100) - ((End - 1) // 100) handles hitting 0 correctly.
            passes = (abs_state // 100) - ((new_abs_state - 1) // 100)

        password += passes
        abs_state = new_abs_state

    # The final dial state is just the absolute state modulo 100
    print(f"Final State: {abs_state % 100}")
    print(f"Password: {password}")

part2_fixed(real_states)