import math

def decompose(n):
    sol, ns, curr = [], n ** 2, n - 1

    while sum(x ** 2 for y, x in sol) != n ** 2 and curr >= 0:

        new = ns - curr ** 2
        # print "curr =", curr, "ns =", ns, "new =", new
        if new >= 0 and curr != 0:
            sol.append((ns, curr))
            ns, curr = new, int(math.sqrt(new))
        # print "Current solution:", sol

        if len(set([y for x, y in sol])) != len([y for x, y in sol])\
            or (new == 0 and curr != 0) or (curr == 0 and new != 0) or new < 0:
            if len(sol) == 0:
                return None
            ns, curr = sol.pop()
            # print "Popped: ns, curr =", ns, curr
            curr -= 1

    return [y for x, y in sol]

if __name__ == "__main__":
    for i in [4, 11, 44, 10, 50]:
        print str(i) + ":"
        r = decompose(i)
        print "Result: ", r, "\n"
