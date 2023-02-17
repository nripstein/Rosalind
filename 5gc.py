

with open("gc.txt") as fh:
    # for line in fh:
    #     print(line.__repr__())
    raw_lines = []
    for line_ in fh:
        raw_lines.append(line_)

    print(raw_lines)


def one_check(dna: str) -> float:
    to_divide = 0
    for letter in dna:
        if letter in ("C", "G"):
            to_divide += 1
    percent = to_divide / len(dna) * 100
    return percent


def identify(raw_file: list) -> list[list]:
    sets = []
    for line in raw_file:
        if line[0] == ">":
            sets.append([line[1:].rstrip()])
        elif len(sets[-1]) == 1:
            sets[-1].append(line.rstrip())
        else:
            # print(sets[-1][-1])
            sets[-1][-1] += line.rstrip()
            # sets[-1][-1].join(line.rstrip())
    return sets

# done and submitted
def whole_thing():
    to_check = identify(raw_lines)
    best = 0
    name = "NONE"
    for sequence in to_check:
        # print(sequence)
        current = one_check(sequence[1])
        # print(f"current = {current}")
        if current > best:
            best = current
            name = sequence[0]
    return name + "\n" + str(best)


# s = "CCACCCTCGTGGTATGGCTAGGCATTCAGGAACCGGAGAACGCTTCAGACCAGCCCGGACTGGGAACCTGCGGGCAGTAGGTGGAAT"
# print(one_check(0, s))
# their_0808 = "CCACCCTCGTGGTATGGCTAGGCATTCAGGAACCGGAGAACGCTTCAGACCAGCCCGGACTGGGAACCTGCGGGCAGTAGGTGGAAT"

# print(identify(raw_lines))
print(whole_thing())
#
# print(one_check(their_0808))
#
# print(len("CCACCCTCGTGGTATGGCTAGGCATTCAGGAACCGGAGAACGCTTCAGACCAGCCCGGAC"))
# print(len(their_0808))

