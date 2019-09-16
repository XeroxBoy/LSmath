def gcd(m, n):
    while m % n != 0:
        yushu = m % n
        m = n
        n = yushu
    return n


print(gcd(56, 24))
