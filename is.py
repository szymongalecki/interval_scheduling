"""
Interval Scheduling

cat in1.txt | python3 is.py
cat in2.txt | python3 is.py
"""


def interval_scheduling():
    S, F = [], []
    res = 0
    n = int(input())

    for _ in range(n):
        s, f = input().split()
        S.append(int(s))
        F.append(int(f))
    F, S = (list(_) for _ in zip(*sorted(zip(F, S))))

    while F:
        f = F.pop(0)
        S.pop(0)
        res += 1
        while S and S[0] < f:
            S.pop(0)
            F.pop(0)
    return res


print(interval_scheduling())
