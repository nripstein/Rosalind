# done and submitted

def timer(func):
    import time
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        end = time.perf_counter()
        print(f"{func.__name__} took {end - start:.6f} seconds")
        return result
    return wrapper


# def finder(dna_sequences: list[str]):
#     shortest_sequence = len(min(dna_sequences, key=len))
#
#     subs = sub_sequences(dna_sequences, shortest_sequence)
#     longest = ""
#     for sub in subs:
#         in_all = True
#         for sequence in dna_sequences:
#             if sub not in sequence:
#                 in_all = False
#         if in_all:
#             if len(sub) > len(longest):
#                 longest = sub
#     return longest
#
#
# def sub_sequences(dna_sequences: list[str], shortest_sequence_len):
#     subs = set()
#     for sequence in dna_sequences:  # make below into nested loop like this and range will be sequence
#         for i in range(len(sequence)):
#             # start at 1 to avoid empty string. +1 to make up for starting at 1
#             for string_length in range(1, shortest_sequence_len + 1):   # by shortest length bc if longer, cant be in that one
#                 subs.add(sequence[i:i + string_length])
#     return subs
#
#
# def finder2(dna_sequences: list[str]):
#     shortest_sequence_len = len(min(dna_sequences, key=len))
#     longest = ""
#     for sequence in dna_sequences:  # make below into nested loop like this and range will be sequence
#         for i in range(len(sequence)):
#             # start at 1 to avoid empty string. +1 to make up for starting at 1. mb start at longest len + 1 to reduce and avoid if in else
#             for string_length in range(1, shortest_sequence_len + 1):   # by shortest length bc if longer, cant be in that one
#                 to_add = sequence[i:i + string_length] # len problem bc len doesnt get updated on str. use other len var to fix
#                 if not all(to_add in s for s in dna_sequences):
#                     break
#                 else:
#                     if len(to_add) > len(longest):
#                         longest = to_add
#     return longest


@timer
def finder3(dna_sequences: list[str]):
    shortest_sequence_len = len(min(dna_sequences, key=len))
    longest = ""
    len_longest = 0
    # print("in")
    for sequence in dna_sequences:  # make below into nested loop like this and range will be sequence
        # print(f"seq = {sequence}")
        for i in range(len(sequence)):
            # start at 1 to avoid empty string. +1 to make up for starting at 1. mb start at longest len + 1 to reduce and avoid if in else
            for string_length in range(len_longest + 1, shortest_sequence_len + 1):   # by shortest length bc if longer, cant be in that one
                to_add = sequence[i:i + string_length]
                if not all(to_add in s for s in dna_sequences):
                    break
                else:
                    if len(to_add) > len(longest):
                        longest = to_add
                        len_longest = len(to_add)
    return longest


@timer
def read_fasta(file_name: str, sequence_only_bool: bool = False) -> tuple:
    def sequence_only(fasta: list) -> set[str]:
        output = set()
        for sequence in fasta:
            output.add(sequence[1])
        return output

    with open(file_name) as fh:
        raw_lines = []
        for line in fh:
            raw_lines.append(line)

    sets = []
    for line in raw_lines:
        if line[0] == ">":
            sets.append([line[1:].rstrip()])
        elif len(sets[-1]) == 1:
            sets[-1].append(line.rstrip())
        else:
            sets[-1][-1] += line.rstrip()

    if not sequence_only_bool:
        return tuple(sets)
    else:
        return tuple(sequence_only(sets))


data = read_fasta("lcsm.txt", True)
# print(data)
# print(finder(data))
print(finder3(data))






