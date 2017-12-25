scores = input().split()

ratio = len(list(filter(lambda score: score == "A", scores)))/len(scores)

print("{:0.2f}".format(ratio))
