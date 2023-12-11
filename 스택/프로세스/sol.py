# 시간 복잡도 문제 있음
from string import ascii_uppercase
from collections import deque

def solution(priorities, location):
    answer = 0
    Alpha_list = list(ascii_uppercase)
    AL_list = deque([Alpha_list[i] for i in range(len(priorities))])
    check = dict(zip(AL_list, priorities))
    my = AL_list[location]
    my_priorities = deque(priorities)
    final = []

    while my_priorities:
        max_priority = max(my_priorities)
        if len(priorities) == 0:
            break

        while check[AL_list[0]] != max_priority:
            AL_list.append(AL_list.popleft())
            my_priorities.append(my_priorities.popleft())

        final.append(AL_list.popleft())
        my_priorities.popleft()

    answer = final.index(my) + 1

    return answer

print(solution([2, 1, 3, 2], 2))
print(solution([1, 1, 9, 1, 1, 1], 0))
