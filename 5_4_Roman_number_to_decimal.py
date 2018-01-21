numbers = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}


def convert(s):
    total = 0
    last = 0

    for n in map(lambda c: numbers[c], reversed(list(s))):
        if n >= last:
            total += n
            last = n
        else:
            total -= n
            last = n

    return total

print(convert(input()))

