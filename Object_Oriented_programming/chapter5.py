import collections.abc
from functools import lru_cache


class Power1(collections.abc.Callable):
    def __call__(self, x, n):
        p = 1
        for i in range(n):
            p = p*x
        return p


class Power2(collections.abc.Callable):
    def __call__(self, x, n):
        p = 1
        for i in range(n):
            p = p*x
        return p


class Power3:
    def __call__(self, x, n):
        p = 1
        for i in range(n):
            p = p*x
        return p


class Power4(collections.abc.Callable):
    def __call__(self, x, n):
        if n == 0:
            return 1
        elif n % 2 == 1:
            return self.__call__(x, n-1) * x
        else:
            t = self.__call__(x, n//2)
            return t * t


class Power5(collections.abc.Callable):
    def __init__(self):
        self.memo = {}

    def __call__(self, x, n):
        if (x, n) not in self.memo:
            if n == 0:
                self.memo[x, n] = 1
            elif n % 2 == 1:
                self.memo[x, n] = self.__call__(x, n-1) * x
            elif n % 2 == 0:
                t = self.__call__(x, n//2)
                self.memo[x, n] = t*t
            else:
                raise Exception('Logic Error')
            return self.memo[x, n]


@lru_cache(None)
def pow6(x, n):
    if n == 0:
        return 1
    elif n % 2 == 1:
        return pow6(x, n-1)*x
    else:
        t = pow6(x, n//2)
        return t*t