from collections import defaultdict, deque

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

# Function to reorder a single update using topological sorting


def reorder_update(update, rules):
    # Build a directed graph for the current update
    graph = defaultdict(list)
    in_degree = defaultdict(int)
    pages_in_update = set(update)

    for x, y in rules:
        if x in pages_in_update and y in pages_in_update:
            graph[x].append(y)
            in_degree[y] += 1
            if x not in in_degree:
                in_degree[x] = 0

    # Topological sort using Kahn's algorithm
    queue = deque([node for node in in_degree if in_degree[node] == 0])
    sorted_order = []

    while queue:
        current = queue.popleft()
        sorted_order.append(current)
        for neighbor in graph[current]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    return sorted_order


# Main logic to find invalid updates and compute the result
middle_sum = 0
for update in updates:
    if not is_valid_update(update, converted_rules):
        # Reorder the update
        corrected_order = reorder_update(update, converted_rules)
        # Find the middle page number
        middle_page = corrected_order[len(corrected_order) // 2]
        middle_sum += middle_page

print(f"The sum of middle page numbers for corrected updates is: {middle_sum}")
