def összeadás(szám1, szám2):
    return szám1 + szám2

def dupla_összeadás(a, b, c ,d):
    return összeadás(a, b) + összeadás(c, d)

összeg = dupla_összeadás(2, 4, 5, 6)

print(összeg)
