
def solution_old(xs):
    product = 0
    largestNegative = None
    negativeCount = 0
    for x in xs:
        if x != 0:
            if product == 0:
                product = x
            else:
                product *= x
        if x < 0:
            negativeCount += 1
            if largestNegative is None:
                largestNegative = x
            elif x > largestNegative:
                largestNegative = x

    if product < 0:
        if negativeCount > 1:
            product /= largestNegative
        else:
            product = 0
    return str(int(product))

def solution(xs):
    if len(xs) == 1:
        return str(xs[0])
    product = 0
    negativeNumbers = []
    for x in xs:
        if x > 0:
            product = x if product == 0 else product * x
        elif x < 0:
            negativeNumbers.append(x)
    negativeNumbers.sort(reverse = True)
    start = 0 if len(negativeNumbers) % 2 == 0 else 1
    for x in negativeNumbers[start:len(negativeNumbers)]:
        product = x if product == 0 else product * x
    return str(product)



assert solution([2, 0, 2, 2, 0]) == "8"
assert solution([-2, -3, 4, -5]) == "60"
assert solution([0, 0, 0]) == "0"
assert solution([-1, 0, 0]) == "0"
assert solution([-1, -2, 0]) == "2"
assert solution([4]) == "4"
assert solution([-1]) == "-1"