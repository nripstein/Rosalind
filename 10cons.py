# done and submitted
def cons(sequences) -> str:
    output = ""
    length = len(sequences[0])
    a = [0 for _ in range(length)]
    c, g, t = a[:], a[:], a[:]
    for letter_index in range(length):
        for sequence in sequences:
            if sequence[letter_index] == "A":
                a[letter_index] += 1
            elif sequence[letter_index] == "C":
                c[letter_index] += 1
            elif sequence[letter_index] == "G":
                g[letter_index] += 1
            elif sequence[letter_index] == "T":
                t[letter_index] += 1

        col = [a[letter_index], c[letter_index], g[letter_index], t[letter_index]]
        # print(col)
        highest = max(col)
        max_index = col.index(highest)
        # print(f"index = {max_index}, max = {highest}")
        index_dict = {0: "A", 1: "C", 2: "G", 3: "T"}

        output += index_dict[max_index]
    output += "\n"
    output += list_to_string_cons(a, "A") + "\n"
    output += list_to_string_cons(c, "C") + "\n"
    output += list_to_string_cons(g, "G") + "\n"
    output += list_to_string_cons(t, "T")
    return output


def sequence_only(fasta: list[list]) -> list[str]:
    output = []
    for sequence in fasta:
        output.append(sequence[1])
    return output


def read_fasta(file_name: str) -> list[list]:
    with open(file_name) as fh:
        raw_lines = []
        for line_ in fh:
            raw_lines.append(line_)

    sets = []
    for line in raw_lines:
        if line[0] == ">":
            sets.append([line[1:].rstrip()])
        elif len(sets[-1]) == 1:
            sets[-1].append(line.rstrip())
        else:
            sets[-1][-1] += line.rstrip()
    return sets


def list_to_string_cons(ls: list, letter: str) -> str:
    output = letter + ": "
    for element in ls:
        output += str(element) + " "
    return output[:-1]


whole_fasta = read_fasta("cons.txt")
s = sequence_only(whole_fasta)
print(cons(s))

