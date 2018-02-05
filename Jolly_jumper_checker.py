def get_jolly_numbers(seq):
    n = len(seq)

    iterator = iter(seq)

    a = next(iterator)
    for i in range(n - 1):
        b = next(iterator)

        yield abs(a - b)

        a = b


seq = list(map(int, input().split()))
print("Jolly" if set(range(1, len(seq))).issubset(set(get_jolly_numbers(seq))) else "Not jolly")
