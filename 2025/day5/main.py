with open("sample.txt") as f:
    sample = f.read()

with open("test.txt") as f:
    test = f.read()


def preprocess(data:str) -> tuple[list[tuple[int, ...]], set[int]]:

    split_data = data.split("\n")
    split_index = split_data.index("")
    ranges: list[tuple[int, ...]] = [
        tuple(map(int, string.split("-")))
        for string in split_data[:split_index]
        ]

    ranges.sort()
    ingredients = set(map(int, split_data[split_index+1:]))

    return (ranges, ingredients)

def get_set(ranges:list[str], ingredients) -> int:

    fresh_numbers_count: int = 0
    ingredients_dup = ingredients.copy()

    for first_range in ranges:
        first_number, last_number = map(int, first_range.split("-"))
        ingredients = ingredients_dup.copy()      
        for number in ingredients:
           if first_number <= number <= last_number:
               fresh_numbers_count += 1
               ingredients_dup.remove(number)

    return fresh_numbers_count

# Part 2
def count_fresh_range(ranges:list[tuple[int, ...]]) -> int:
    count = 0
    highest_number: int = -999999999999999
    for working_range in ranges:
        if not highest_number > working_range[0]:
            highest_number = working_range[0]
        count += max(0, working_range[1] - highest_number + 1)
        if highest_number < working_range[1] + 1:
            highest_number = working_range[1] + 1

    return count

if __name__ == "__main__":
    data = test

    ranges, _ = preprocess(data)
    fresh_numbers = count_fresh_range(ranges)
    print("COUNT IS:")
    print(fresh_numbers)

