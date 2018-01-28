s = input()


def solve(a, b, koefs):
    (c, d) = divmod(a, b)  # (7, 29)
    koefs.append(c)

    if d > 0:
        solve(b, d, koefs)

    return koefs

print(" ".join([str(k) for k in solve(int(s.split("/")[0]), int(s.split("/")[1]), [])]))
