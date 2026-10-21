with open("sample.txt", "r") as file:
    sample: list[str] = []
    for line in file:
        sample.extend(line.strip().split(","))

with open("test.txt", "r") as file:
    test: list[str] = []
    for line in file:
        test.extend(line.strip().split(","))


invalid_numbers: list[int] = []

def is_invalid(number: int) -> bool:
    s = str(number)
    n = len(s)

    for size in range(1, n // 2 + 1):
        if n % size == 0:
            pattern = s[:size]
            if pattern * (n // size) == s:
                return True
    return False

for line in test:
    if line == "":
        continue
    first_number, last_number = line.split("-")
    for i in range(int(first_number), int(last_number) + 1):
        if is_invalid(i):
            invalid_numbers.append(i)

print(f"The final sum is {sum(invalid_numbers)}")