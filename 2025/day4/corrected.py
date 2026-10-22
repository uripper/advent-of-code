with open("sample.txt", "r") as file:
    sample = file.read().split("\n")

with open("test.txt", "r") as file:
    test = file.read().split("\n")

def solve(data: list[str]) -> int:
    grid = [list(row) for row in data if row]
    height = len(grid)
    width = len(grid[0])

    result = 0

    while True:
        removable: list[tuple[int,int]] = []

        for row in range(height):
            for col in range(width):
                if grid[row][col] != "@":
                    continue

                neighbors = 0

                for dr in (-1, 0, 1):
                    for dc in (-1, 0, 1):
                        if dr == 0 and dc == 0:
                            continue

                        nr = row + dr
                        nc = col + dc

                        if (
                            0 <= nr < height 
                            and 0 <= nc < width 
                            and grid[nr][nc] == "@"
                        ):
                            neighbors += 1

                if neighbors < 4:
                    removable.append((row, col))

        if not removable:
            break

        for row, col in removable:
            grid[row][col] = "."

        result += len(removable)

    return result

if __name__ == "__main__":
    print(solve(test))