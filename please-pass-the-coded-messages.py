def solution(l):
    l.sort(reverse = True)
    digitSum = sum(l)

    if digitSum % 3 == 0:
        return concat_digits(l)

    mod1Digits = []
    mod2Digits = []

    for digit in l:
        if digit % 3 == 1:
            mod1Digits.append(digit)
        elif digit % 3 == 2:
            mod2Digits.append(digit)

    if digitSum % 3 == 1:
        if len(mod1Digits) > 0:
            l.remove(mod1Digits[len(mod1Digits)-1])
        else:
            l.remove(mod2Digits[len(mod2Digits)-1])
            l.remove(mod2Digits[len(mod2Digits)-2])
    elif digitSum % 3 == 2:
        if len(mod2Digits) > 0:
            l.remove(mod2Digits[len(mod2Digits)-1])
        else:
            l.remove(mod1Digits[len(mod1Digits)-1])
            l.remove(mod1Digits[len(mod1Digits)-2])
    
    return concat_digits(l)
        

def concat_digits(D):
    if D == []:
        return 0
    final = ""
    for digit in D:
        final += str(digit)
    return int(final)

print(solution([3, 1, 4, 1]))
assert solution([3, 1, 4, 1]) == 4311
assert solution([3, 1, 4, 1, 5, 9]) == 94311
assert solution([3]) == 3
assert solution([1]) == 0
assert solution([1,1]) == 0