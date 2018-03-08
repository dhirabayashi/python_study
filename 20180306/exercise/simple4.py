from functools import reduce


def lcm(a, b):
    def is_common_divisor(c, d, div):
        return c % div == 0 and d % div == 0

    def is_continue(e, f):
        for i in range(2, min(e, f) + 1):
            if is_common_divisor(e, f, i):
                return True

        else:
            return False

    divisors = []

    while is_continue(a, b):
        to = min(a, b)
        for j in range(2, to):
            if is_common_divisor(a, b, j):
                divisors.append(j)
                a = a // j
                b = b // j
                break

    return reduce(lambda x, y: x * y, divisors) * a * b


print(lcm(12, 42))
