import math

def solution_(x, y):
    m = int(x)
    f = int(y)
    generations = 0
    while m > 1 or f > 1:
        factor = 1
        if m > f:
            factor = math.ceil(m / f) - 1
            m -= f * factor
        elif m < f:
            factor = math.ceil(f / m) - 1
            f -= m * factor
        else:
            return "impossible"
        generations += factor
    return str(generations)

def solution(x, y):
    m = int(x)
    f = int(y)
    generations = 0
    while m > 1 or f > 1:
        factor = 1
        if m > f:
            factor = int(math.ceil(float(m) / f)) - 1
            m -= f * factor
        elif m < f:
            factor = int(math.ceil(float(f) / m)) - 1
            f -= m * factor
        else:
            return "impossible"
        generations += factor
    return str(generations)

assert solution('4', '7') == "4"
assert solution('2', '1') == "1"
assert solution('2232132132', '1') == "2232132131"
assert solution('2232132132', '2') == "impossible"
assert solution('96', '5') == "23"
assert solution('2', '4') == "impossible"