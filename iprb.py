
def sol(ls: list[int]):  # can't jsut do total alleles
    homo_dominant, hetero, homo_recessive = ls
    # dom_alleles = homo_dominant * 2 + hetero
    # rec_alleles = homo_recessive * 2 + hetero
    # print(dom_alleles / (dom_alleles + rec_alleles))
    p_homo_dominant = homo_dominant / (hetero + homo_recessive + homo_dominant)
    p_hetero_and_dominant_passed = hetero / (hetero + homo_recessive + homo_dominant) + (0.5 * hetero / (hetero + homo_recessive + homo_dominant))
    print(p_homo_dominant, p_hetero_and_dominant_passed)
    print(p_homo_dominant + p_hetero_and_dominant_passed)
    # ok idk


def input_parse(inp: str):
    return [int(i) for i in inp.split(" ")]


a = input_parse("2 2 2")
print(a)
sol(a)
