def recursion1(m):
    if m <= 0:  # 递归终止条件
        return 1
    else:
        return m * recursion1(m // 2)


def recursion2(m):
    mult = 1
    while m > 0:
        mult = mult * m
        m = m // 2
    return mult


def akm(m, n):
    if m == 0:
        return n + 1
    if m != 0 and n == 0:
        return akm(m - 1, 1)
    return akm(m - 1, akm(m, n - 1))


def recursion3(x, n):
    if n == 0:
        return 1
    if n == 1:
        return x
    if n > 1:
        return ((2*n-1)*x*recursion3(x, n-1) - (n-1)*recursion3(x, n-2))/n


if __name__ == '__main__':
    # print(recursion1(4))
    # print(recursion2(4))
    # print(akm(2, 2))
    s = ['5', '2', '1']
    ss = int(''.join(s))
    print(ss)
    print(type(ss))
    print(list(str(ss)))
    pass