n = int(input())


def f(x):
    return x * x


cache = {}
for v in range(n):
    val = input()
    if val not in cache:
        cache[val] = f(val)

    print(cache[val])
