def count(s):
    stats = dict()

    for word_len in map(lambda word: len(word), s.split(" ")):
        if word_len in stats:
            stats[word_len] += 1
        else:
            stats[word_len] = 1
    return stats

stats = count(input())

for k in sorted(stats):
    print(str(k) + ": " + str(stats[k]))

