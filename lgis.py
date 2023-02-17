
# Given: A positive integer n≤10000 followed by a permutation π of length n.
# Return: A longest increasing subsequence of π, followed by a longest decreasing subsequence of π.

# example: input
# 5
# 5 1 4 2 3
# output:
# 1 2 3
# 5 4 2


def str_to_list(inp: str) -> list:
    string_elements = inp.split(" ")
    output = []
    for i in string_elements:
        output.append(int(i))
    return output


def longest(inp: list[int]):
    # did this wrong bc they don't need to be adjascent
    output = []
    # for sequence_length in range(len(inp)):
    #     for number_index in range(len(inp)):
    #         pass

    # start with 1 length check
    sequence_length = 3
    for number_index in range(len(inp) - sequence_length + 1):
        candidate = inp[number_index: number_index + sequence_length]
        print(candidate)
        if increasing(candidate) and len(candidate) > len(output):
            output = candidate

    return output


def increasing(inp: list[int]) -> bool:
    for num in range(len(inp) - 1):
        if inp[num] >= inp[num + 1]:
            return False
    return True


def att2(ls: list):
    longest_increasing = []
    longest_decreasing = []
    # set first element. end up doing this in loop
    current_start_index = 0

    longest_increasing.append(ls[current_start_index])
    longest_decreasing.append(ls[current_start_index])
    for i in range(current_start_index, len(ls)):
        if ls[i] > longest_increasing[-1]:
            longest_increasing.append(ls[i])
        if ls[i] < longest_decreasing[-1]:
            longest_decreasing.append(ls[i])

    return longest_decreasing, longest_decreasing


def att3(ls: list):
    longest_increasing = []
    longest_decreasing = []
    # set first element. end up doing this in loop
    current_start_index = 0

    # longest_increasing.append(ls[current_start_index])
    # longest_decreasing.append(ls[current_start_index])

    ls_increasing_copy = ls[:]
    ls_decreasing_copy = ls[:]
    # for i in range(current_start_index, len(ls)):
    #     if len(ls_increasing_copy) > 1:
    #         # print(ls_increasing_copy)
    #         max_index = ls_increasing_copy.index(max(ls_increasing_copy))
    #         p = ls_increasing_copy.pop(max_index)
    #         print(p)
    #         longest_increasing.append(p)

    i = current_start_index
    while i < len(ls):
        if len(ls_increasing_copy) > 1:
            # print(ls_increasing_copy)
            max_index = ls_increasing_copy.index(max(ls_increasing_copy))
            p = ls_increasing_copy.pop(max_index)
            ls_increasing_copy = ls_increasing_copy[max_index:]
            print(ls_increasing_copy)
            # print(p)
            longest_increasing.append(p)

            i = max_index
            print(f"i = {i}, max index = {max_index}, lscopy = {ls_increasing_copy}")

        if len(ls_decreasing_copy) > 1:
            min_index = ls_decreasing_copy.index(min(ls_decreasing_copy))
            p = ls_increasing_copy.pop(min_index)
            ls_decreasing_copy = ls_decreasing_copy[min_index:]
            longest_decreasing.append(p)

        i += 1

    return longest_increasing





# 6474276001
# go to walk in clinic. buy from pharmacy and then go to walk in clinic and have them send it to them for records
# print(str_to_list("5 1 4 2 3"))

sample_input = "5 1 4 2 3"


# print(longest(str_to_list(sample_input)))
print(att3(str_to_list(sample_input)))

