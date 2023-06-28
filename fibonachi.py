cache = {}

def fibo(n):
    # fibo.iter += 1
    if n in cache.keys():
        return cache[n] 
    
    if n == 1 or n == 2:
        cache[n] = 1
        return 1
    
    res = fibo(n - 1) + fibo(n - 2)
    cache[n] = res
    return res

x = int(input("Введите число n: "))
# fibo.iter = 0

if __name__ == '__main__':
    generFibo = [fibo(i) for i in range(1, x)]
    generatorVar = iter(generFibo)
    while (True):
        try:
            print(next(generatorVar))
        except StopIteration:
            break

    