import math

with open("sample.txt", "r") as f:
    sample = f.read().splitlines()
    
    
with open("test.txt", "r") as f:
    test = f.read().splitlines()


def process(data, length_of_array, working_arrays):
    for line in data:
        numbers = [number for number in line.split(" ") if number.strip()]
        if not length_of_array:
            length_of_array = len(numbers)
        working_arrays.append(numbers)
    return working_arrays, length_of_array

def ceph_process(data, length_of_array, working_arrays):
    width = max(map(len, data))
    rows = [row.ljust(width) for row in data]
    columns = []

    for i in range(width - 1, -1, -1):
        column = "".join(row[i] for row in rows[:-1])
        columns.append(column.replace(" ", ""))

    operands = [char for char in rows[-1] if char in "+*"][::-1]

    curr = []
    for number in columns:
        if number == "":
            working_arrays.append(curr)
            curr = []
        else:
            curr.append(number)

    working_arrays.append(curr)

    length_of_array = len(working_arrays)

    return working_arrays, length_of_array, operands

def get_summation(length_of_array, working_arrays, operands):
    total_sum = 0
    for i in range(length_of_array):
        operand = operands[i]
        elements = [int(num) for num in working_arrays[i]]
        if operand == "+":
            total_sum += sum(elements)
        elif operand == "*":
            total_sum += math.prod(elements)
    return total_sum

if __name__ == "__main__":
    data = test

    length_of_array = None
    working_arrays = []

    working_arrays, length_of_array, operands = ceph_process(
        data, length_of_array, working_arrays
    )
    total_sum = get_summation(length_of_array, working_arrays, operands)
    print(total_sum)
