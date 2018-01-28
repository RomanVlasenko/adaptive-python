s = input()


#  239/30
def solve(a, d, koefs):  # (239/30) -> (30/29) -> (29/1)
    (n, r) = divmod(a, d)  # (7, 29) -> (1, 1) -> (29, 0)
    koefs.append(n)  # 7 -> 1 -> 29

    if r > 0:
        solve(d, r, koefs)

    return koefs


print(" ".join([str(k) for k in solve(int(s.split("/")[0]), int(s.split("/")[1]), [])]))
