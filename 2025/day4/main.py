with open("sample.txt", "r") as file:
    sample = file.read().split("\n")

with open("test.txt", "r") as file:
    test = file.read().split("\n")

# @ is a toilet paper roll. 
# If a toilet paper roll has less than 4 it can be picked
adjacency = 4
# We need to count how many rolls of paper than can be picked
result = 0

# If we have a hashmap that counts the adjacency where the key is the position by coordinates
# Determine adjacency by finding all other spots that are 1 at most 1 away on x and/or y

# (1,0) (2,0) (3,0)
# (1,1) (2,1) (3,1)
# (1,2) (2,2) (3,2)

sample_set = {2, 3, 5, 6, 8, 10, 26, 40, 49, 70, 90, 92, 98}
left_cache: set[int] = set()
right_cache: set[int] = set()



def get_coordinates(data: list[str]) -> list[int]:
    coordinates: list[int] = []
    index = 0
    for line in data:
        for character in line:
            if character == "@":
                coordinates.append(index)
            index += 1
    return coordinates

def get_tuple_difference(data: list[str], coordinates: list[int]) -> dict[int,int]:
    counts: dict[int, int] = {}
    line_length = len(data[0])
    for number in coordinates:
        counts[number] = counts.get(number, 0)
        for comparison in coordinates:
            if number == comparison:
                continue
            if number - line_length - 1 > comparison:
                continue
            if number + line_length + 1 < comparison:
                break
            is_adjacent = check_adjacent(number, comparison, line_length)
            if is_adjacent:
                counts[number] = counts.get(number, 0) + 1
    return counts

def check_adjacent(number: int, comparison: int, line_length: int) -> bool:
    number_is_left, number_is_right = get_edges(number, line_length)
    comparison_is_left, comparison_is_right = get_edges(comparison, line_length)

    if (number_is_left and comparison_is_right) or (comparison_is_left and number_is_right):
        return False

    if abs(number - comparison) == 1:
        return True

    if abs((number - line_length) - comparison) <= 1:
        return True

    if abs((number + line_length) - comparison) <=1:
        return True

    return False
        

def get_edges(number:int, line_length:int) -> tuple[bool, bool]:
    is_left: bool = False
    is_right: bool = False
    if number in left_cache:
        is_left = True
    elif number in right_cache:
        is_right = True
    elif number % line_length == 0:
        is_left = True
        left_cache.add(number)
    elif number % line_length == line_length - 1:
        is_right = True
        right_cache.add(number)
    return (is_left, is_right)

def replace_character(data: list[str], numbers_to_replace: set[int]) -> list[str]:
    list_length = len(data[0])
    working_data = "".join(data)
    for index in numbers_to_replace:
        working_data = working_data[:index] + "." + working_data[index+1:]
    new_data = [working_data[i:i+list_length] for i in range(0, len(working_data), list_length)]
    return new_data



if __name__ == "__main__":
    data = test

    while True:
        coordinates = get_coordinates(data)
        counts = get_tuple_difference(data, coordinates)
        total = [value for value in counts.values() if value < adjacency]
        real_counts = {k: v for k, v in counts.items() if v < adjacency}
        keys = real_counts.keys()
        set_keys = set(keys)
        result += len(total)
        if len(total) == 0:
            break
        data = replace_character(data, set_keys)
    print(result)
