with open("sample.txt") as f:
    sample = f.read()

with open("test.txt") as f:
    test = f.read()


def preprocess(data: str) -> tuple[list[tuple[int, int]], set[int]]:
    lines = data.strip().splitlines()
    split_index = lines.index("")

    ranges: list[tuple[int, int]] = []
    for line in lines[:split_index]:
        start, end = map(int, line.split("-"))
        ranges.append((start, end))

    ranges.sort()

    ingredients = set(map(int, lines[split_index + 1:]))

    return ranges, ingredients

# Part 1
def count_fresh_ingredients(
    ranges: list[tuple[int, int]],
    ingredients: set[int]
) -> int:
    return sum(
        any(start <= ingredient <= end for start, end in ranges)
        for ingredient in ingredients
    )

# Part 2
def count_fresh_range(ranges:list[tuple[int, ...]]) -> int:
    count = 0
    highest_number: int = -999999999999999
    for working_range in ranges:
        highest_number = max(highest_number, working_range[0])
        count += max(0, working_range[1] - highest_number + 1)
        if highest_number < working_range[1] + 1:
            highest_number = working_range[1] + 1

    return count

if __name__ == "__main__":
    ranges, ingredients = preprocess(test)

    print(f"Part 1: {count_fresh_ingredients(ranges, ingredients)}")
    print(f"Part 2: {count_fresh_range(ranges)}")
