def handling_file():
    with open('text.txt', 'r') as file:
       grid = [line.strip() for line in file]
    return grid

def part1():
    grid = handling_file()

    count = 0

    for r in range(len(grid)):
        try:
            for c in range(len(grid[0])):
                if grid[r][c] == 'X': continue
                for dr in [-1,0,1]:
                    for dc in [-1,0,1]:
                        if dr  == dc == 0: continue
                        if not (0 <= r + 3 * dr < len(grid) and 0 <= c + 3 *dc < len(grid[0])): continue
                        if grid[r + dr][c + dc] == "M" and grid[r + 2 *dr][c + 2 * dc] == "A" and grid[r + 3 * dr][c + 3 *dc] == "S":
                            count += 1
        except IndexError:
            continue
    return count
                

sol = part1()
print(f'Part1 sol: {sol}')


def part2():
    grid = handling_file()
    count = 0

    for r in range(1, len(grid) - 1):
        try:

            for c in range(1, len(grid[0]) - 1):
                if grid[r][c] != "A":
                    continue
                corners = [grid[r-1][c-1], grid[r-1][c+1], grid[r+1][c+1], grid[r+1][c-1]]
                if "".join(corners) in ["MMSS", "MSSM", "SSMM", "SMMS"]:
                    count += 1
        except IndexError:
            continue
    return count


sol2 = part2()
print(f'Part2 sol: {sol2}')
