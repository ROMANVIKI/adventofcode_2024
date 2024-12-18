# Parse input data
xy_order = []  # Updates
ordering_rules = []  # Rules

with open('example_case.txt', 'r') as file:
    grid = [line.strip() for line in file]

# Separate ordering rules and update sequences
for data in grid:
    if '|' in data:
        ordering_rules.append(data)
    elif len(data) > 0:
        xy_order.append(data)

# Convert ordering rules to a usable format
converted_rules = [tuple(map(int, item.split('|'))) for item in ordering_rules]
updates = [list(map(int, update.split(','))) for update in xy_order]

# Function to validate the order of a single update


def is_valid_update(update, rules):
    for x, y in rules:
        if x in update and y in update:
            # Ensure x comes before y in the update sequence
            if update.index(x) > update.index(y):
                return False
    return True


# Main logic to validate updates and compute the result
middle_sum = 0
for update in updates:
    if is_valid_update(update, converted_rules):
        # Find the middle page number
        middle_page = update[len(update) // 2]
        middle_sum += middle_page

print(
    f"The sum of middle page numbers for correctly ordered updates is: {middle_sum}")
