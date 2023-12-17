import collections
def solution(clothes):
    answer = 0
    codi = len(clothes)
    item = []
    for i in clothes:
        item.append(i[1])
    my_dict = dict(collections.Counter(item))
    if len(my_dict) >= 2:
        johap = 1
        for value in my_dict.values():
            johap *= value
        answer = codi + johap
    else:
        answer = codi

    return answer

print(solution([["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]))
print(solution([["crow_mask", "face"], ["blue_sunglasses", "face"], ["smoky_makeup", "face"]]))


import collections
def solution(clothes):
    answer = 1
    item = []
    for i in clothes:
        item.append(i[1])
    my_dict = dict(collections.Counter(item))
    for value in my_dict.values():
        answer *= (value+1)
    answer = answer -1

    return answer

print(solution([["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]))
print(solution([["crow_mask", "face"], ["blue_sunglasses", "face"], ["smoky_makeup", "face"]]))