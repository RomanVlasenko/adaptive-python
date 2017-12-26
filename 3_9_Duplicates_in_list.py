numbers = input().split()
numbers_set = set()
duplicates = set()

for n in numbers:
    if n in numbers_set:
        duplicates.add(n)
    else:
        numbers_set.add(n)

print(" ".join(duplicates))
