
with open("sample.txt", "r") as f:
    sample = f.readlines()

with open("test.txt", "r") as f:
    test = f.readlines()

with open("mine.txt", "r") as f:
    mine = f.readlines()


def preprocess(line: str) -> int:
    direction = line[:1]
    adjustment = line[1:]
    if direction == "L":
        adjustment = -1 * int(adjustment)
    else:
        adjustment = int(adjustment)
    return adjustment

def normalize(number: int) -> int:
    if number > 99 or number < 0:
        number = number % 100
    return number


def get_count(number: int, prev_number: int, count: int, started_at_zero: bool) -> int:
    adjustment = number - prev_number

    if adjustment > 0:
        count += (prev_number + adjustment) // 100
    elif adjustment < 0:
        count += (abs(adjustment) + (100 - prev_number) % 100) // 100

    return count

def main_process(line: str, working_number: int, count: int) -> tuple[int, int]:
    started_at_zero = False
    print(f"\n{'─' * 45}")
    print(f"  START  {working_number:>3}  |  MOVE  {line.strip():>5}")
    adjustment = preprocess(line)
    if working_number == 0:
        started_at_zero = True
    prev_number = working_number
    working_number += adjustment
    count = get_count(
        working_number,
        prev_number,
        count, 
        started_at_zero
        )
    working_number= normalize(working_number)
    print(f"  END    {working_number:>3}  |  TOTAL {count:>5}")
    return working_number, count



if __name__ == "__main__":
    count = 0
    working_number = 50
    for line in sample:
        working_number, count = main_process(line, working_number, count)
    
    count: int = 0
    working_number: int = 50
    for line in mine:
        working_number, count = main_process(line, working_number, count)

    count = 0
    working_number = 50
    for line in test:
        working_number, count = main_process(line, working_number, count)


    print(f"\n{'═' * 45}")
    print(f"  FINAL COUNT: {count}")
    print(f"{'═' * 45}")
