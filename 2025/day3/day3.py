with open("sample.txt", "r") as f:
    sample = f.read().split("\n")
    
with open("test.txt", "r") as f:
    test = f.read().split("\n")

def find_max(sequence, sequence_length):
    result = ""
    work_seq_len = sequence_length
    last_index = 0
    while len(result) < sequence_length:
        if work_seq_len > 1:
            working_list = sequence[last_index:-(work_seq_len-1)]
        else:
            working_list = sequence[last_index:]
        # print("Working list: ", working_list)
        newest_num = str(max(working_list))
        result += newest_num        
        last_index += working_list.index(newest_num) + 1 
        work_seq_len -= 1
    return result


sequence_length = 12
total = 0
for sequence in sample:
    print("Sequence: ", sequence)
    result = find_max(sequence, sequence_length)
    print("Result: ", result)
    print("Length of result: ", len(result))
    total += int(result)
    

print("Sample total: ", total)

total = 0
for sequence in test:
    # print("Sequence: ", sequence)
    result = find_max(sequence, sequence_length)
    total += int(result)


print("Test total: ", total)
