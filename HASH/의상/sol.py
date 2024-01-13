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
    my_dict = dict(collections.Counter(item)) ## dict를 안씌우면 Counter{key:value}형태로 나와서 dict를 씌워줘야함
    print(my_dict)
    for value in my_dict.values():
        answer *= (value+1)
    answer = answer -1

    return answer

print(solution([["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]))
print(solution([["crow_mask", "face"], ["blue_sunglasses", "face"], ["smoky_makeup", "face"]]))

# (x+a)(x+b)(x+c) = x3 + (a+b+c)x2 + (ab+bc+ca)x + (abc)라는 식이 정립됩니다. 총 조합의 개수가 계수에 다 포함되어있음
# 그 후 맨 앞 x3 의 계수는 정답에 포함되지 않으므로 마지막에 1을 빼준다.

# 근데 이것도 왜 hash문제인지? 수학공식에 가까운 문제