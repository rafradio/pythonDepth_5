names = ["доходный", "классический", "выгодный"]
base = [10000, 10000, 10000]
rate = ["10.25%", "8.25%", "12.25%"]

# def genRate(names: list[str], base: list[int], rate: list[str]):
#     for i in range(len(names)):
#         yield {names[i]: base[i] * float(rate[i][0: -1]) / 100}

if __name__ == '__main__':
    # genRate = map(lambda i: {names[i]: base[i] * float(rate[i][0: -1]) / 100}, range(len(names)))
    genRate1 = [{names[i]: base[i] * float(rate[i][0: -1]) / 100} for i in range(len(names))]
    generatorVar = iter(genRate1)
    while (True):
        try:
            print(next(generatorVar))
        except StopIteration:
            break