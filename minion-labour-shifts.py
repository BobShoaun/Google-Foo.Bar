


def solution (data : list, n : int):
    counts : dict = {}

    for i in range(0, len(data)):
        if data[i] in counts:
            counts[data[i]] += 1
        else:
            counts[data[i]] = 1
    
    for key, value in counts.items():
        if value > n:
            data = list(filter(lambda d: d != key, data))

    return data

def solution2 (data: list, n: int):

    occurences :dict = {}

    for i in range(0, len(data)):
        if data[i] in occurences:
            if occurences[data[i]] > n:
                continue
            occurences[data[i]] += 1
        else:
            occurences[data[i]] = 1
        
        

    return data
    

print(solution([1, 2, 3], 0))
assert solution([1, 2, 3], 0) == []
assert solution([1, 2, 2, 3, 3, 3, 4, 5, 5], 1) == [1, 4]
assert solution([], 1) == []

# print(solution([1, 2, 2, 1, 3], 2))