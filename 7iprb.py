
# NOT DONE IDK
def iprb(dominant: int, hetero: int, recessive: int) -> float:
    total_population = dominant + hetero + recessive

    mating_pairs = 0

    mating_pairs += (total_population - 1) * dominant
    mating_pairs += (total_population - 1) * hetero
    mating_pairs += (total_population - 1) * recessive
    # print(mating_pairs)

    dominant_alleles = dominant * 2
    dominant_alleles += hetero

    recessive_alleles = recessive * 2
    recessive_alleles += hetero
    # print(dominant_alleles/recessive_alleles)

    recessive_list = [False for _ in range(recessive_alleles)]
    dominant_list = [True for _ in range(dominant_alleles)]
    # print(dominant_list)
    # print(recessive_list)

    # create an empty matrix


    total = (total_population - 1) * dominant  # all dominant mating pairs yield dominant kid

    return 0.0


def simulate(dominant: int, hetero: int, recessive: int):
    import random
    total_population = dominant + hetero + recessive
    weights = [dominant/total_population, hetero/total_population, recessive/total_population]
    options = ["d", "h", "c"]

    # element = random.choices(options, weights=weights)[0]
    chosen = random.choices(options, weights=weights, k=2)
    print(chosen)
    if "d" in chosen:
        return 1




print(iprb(2, 2, 2))
# print(iprb(1, 1, 0))
simulate(2, 2, 2)




