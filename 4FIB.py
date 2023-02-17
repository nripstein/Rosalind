# what it wanted was pretty confusing. submitted
# do per gen on -2 bc -1 is still a kid I think
def main(inp: str) -> int:
    months, per_gen = inp.split(" ")

    ls = [1, 1]
    for i in range(2, int(months)):
        ls.append(int(per_gen)*(ls[i - 2]) + ls[i - 1])
    print(ls)
    return ls[-1]

a = "33 2"
print(main(a))



