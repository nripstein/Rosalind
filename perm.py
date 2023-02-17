from math import factorial


def perm(n):
    output = [[] for _ in range(factorial(n))]
    to_check = [i + 1 for i in range(n)]
    for num_index in range(len(to_check)):
        print(num_index)

    return to_check


def recursive_att1(ls: list):
    print(f"ls = {ls}")
    # if not ls:
    #     return []
    # if len(ls) == 1:
    #     return ls[0]
    if len(ls) == 2:
        return [ls[0], ls[1]]
    else:
        return [ls[-1], recursive_att1(ls[:-1])]


# idea:
# hold 0 posn and 1 posn and... till last two, then swap last two
# then switch around 1 and 2 and then add 3 into it


# so it needs to be recursive where I can have it return all perms of list of len 3


def recursive_att2(ls: list):
    pass


def shuffle_1_more(previously_shuffled: list, new_element): # works!
    output = set()
    for option in previously_shuffled:
        for index in range(len(previously_shuffled) + 1):
            tmp = option[:]
            tmp.insert(index, new_element)
            output.add(tuple(tmp))
    return ls_ls(output)


def handler(n: int):
    to_slice = [i + 1 for i in range(n)]
    output = []
    first = to_slice[:1]  # just [1] always
    second = shuffle_1_more([first], 2)

    first_output = []
    for tup in second:
        first_output.append(list(tup))
    output.append(first_output)

    for i in range(1, len(to_slice)):
        # print(i)
        to_append_raw = shuffle_1_more(list(output[i - 1]), i + 1)
        # print(to_append_raw)
        to_append_proper = []
        for tup in to_append_raw:
            to_append_proper.append(list(tup))
        output.append(to_append_proper)

    final = []
    for i in output:
        print(len(i))

    return output


def ls_ls(the_set: set[tuple]):
    output = []
    for element in the_set:
        output.append(list(element))
    return output


def handler_att2(n: int):
    all_subsets = [[[1, 2], [2, 1]]]

    for i in range(n - 2):
        input_list = all_subsets[-1]
        to_add = shuffle_1_more(input_list, len(input_list[-1]) + 1)
        all_subsets.append(to_add)
        # print(input_list)
        # print(output)

    return all_subsets[-1]


def list_to_string(ls: list) -> str:
    output = ""
    for element in ls:
        output += str(element) + " "
    return output[:-1]


def stringify(list_of_lists: list[list]):
    output = str(len(list_of_lists)) + "\n"
    for ls in list_of_lists:
        output += list_to_string(ls) + "\n"
    return output.rstrip()


# print(handler_att2(4))
print(stringify(handler_att2(7)))
# print(handler(4))
# print(shuffle_1_more([[1]], 2))
# print(handler(3))
# print(perm(3))
# print(recursive_att1([1, 2, 3, 4]))
# print(shuffle_1_more([[1, 2], [2, 1]], 3))
p = (shuffle_1_more([[3, 2, 1], [2, 3, 1], [2, 1, 3], [3, 1, 2], [1, 3, 2], [1, 2, 3]], 4))
# print(p)
# print(ls_ls(p))
# print(p)
# print(len(p))
# print("==")

ans = [
[1, 2, 3, 4],
[1, 2, 4, 3],
[1, 3, 2, 4],
[1, 3, 4, 2],
[1, 4, 2, 3],
[1, 4, 3, 2],
[2, 1, 3, 4],
[2, 1, 4, 3],
[2, 3, 1, 4],
[2, 3, 4, 1],
[2, 4, 1, 3],
[2, 4, 3, 1],
[3, 1, 2, 4],
[3, 1, 4, 2],
[3, 2, 1, 4],
[3, 2, 4, 1],
[3, 4, 1, 2],
[3, 4, 2, 1],
[4, 1, 2, 3],
[4, 1, 3, 2],
[4, 2, 1, 3],
[4, 2, 3, 1],
[4, 3, 1, 2],
[4, 3, 2, 1]
]

# p_set = set()
# for i in p:
#     p_set.add(tuple(i))
# print(p)
# print(len(p_set))
# print("here")

# ans_set = set()
# for i in ans:
#     ans_set.add(tuple(i))

# print(p_set)
# print(ans_set)
#
# print(len(p_set))
# print(len(ans_set))
# print(p_set == ans_set)
#
# for i in ans:
#     print(i)
#
# q = sorted(p_set, key=lambda x: (x[0], x[1], x[3]))
# print("---")
# for i in q:
#     print(i)
# print(q)
#

def recursive_att3(n_list):
    output = []
    if len(n_list) == 2:
        return [n_list[1], n_list[0]]
    else:
        output.append(recursive_att3(n_list[:-1]))
    return output


# print(recursive_att3([1, 2, 3, 4]))

# print(shuffle_1_more([[2,1], [1, 2]], 3))

