import math

with open("sample.txt", "r") as f:
    sample = f.read().splitlines()

with open("test.txt", "r") as f:
    test = f.read().splitlines()


def parse_part_one(data):
    number_rows = [
        [int(number) for number in row.split()]
        for row in data[:-1]
    ]

    problems = [
        list(numbers) for numbers in zip(*number_rows)
    ]
    operators = data[-1].split()

    return problems, operators


def parse_part_two(data):
    width = max(map(len, data))
    padded_rows = [row.ljust(width) for row in data]

    problems = []
    current_problem = []

    for column_index in range(width - 1, -1, -1):
        number = "".join(
            row[column_index] for row in padded_rows[:-1]
        ).replace(" ", "")

        if number:
            current_problem.append(int(number))
        elif current_problem:
            problems.append(current_problem)
            current_problem = []

    if current_problem:
        problems.append(current_problem)

    operators = [
        character
        for character in reversed(padded_rows[-1])
        if character in "+*"
    ]

    return problems, operators


def calculate_total(problems, operators):
    total = 0

    for numbers, operator in zip(problems, operators, strict=True):
        if operator == "+":
            total += sum(numbers)
        elif operator == "*":
            total += math.prod(numbers)

    return total


if __name__ == "__main__":
    data = test

    part_one_problems, part_one_operators = parse_part_one(data)
    part_two_problems, part_two_operators = parse_part_two(data)

    print("Part 1:", calculate_total(part_one_problems, part_one_operators))
    print("Part 2:", calculate_total(part_two_problems, part_two_operators))