from collections import Counter

words = input().lower().split()
for word, num in Counter(words).items():
    print(word, num)