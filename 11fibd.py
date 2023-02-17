# NOT DONE, IDK

def att2(inp: str):
    months, life_span = inp.split(" ")
    months, life_span = int(months), int(life_span)
    ls = [1, 1]
    for i in range(2, months):
        ls.append(ls[i-2] + ls[i-1])

    new = ls[:len(ls) - life_span]
    print(ls)
    print(new)
    # print(new)
    # print(sum(new))
    return sum(new)

# FROM INTERNET
def fib(month, age):
    generation = [0]*age
    generation[0], generation[1] = 0,1

    for x in range(2,month):
        temp = list(generation)
        # print(generation)
        generation[0] = sum(generation[1:]) #number of new born

        # print(generation[0])
        for i in range(1,age):
            generation[i] = temp[i-1]
    # print(generation)
    return sum(generation)
# print(att2("6 3"))
a = "81 16" # was wrong
# print(att2(a))
print(att2("6 3"))
# print("---")
# print(fib(6, 3))

