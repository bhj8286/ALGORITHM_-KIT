from string import ascii_uppercase
def solution(priorities, location):
    answer = 0
    Alpha_list = list(ascii_uppercase)
    AL_list = []
    for i in range(len(priorities)):
        AL_list.append(Alpha_list[i])
    check = dict(zip(AL_list, priorities))
    print(AL_list)
    my = AL_list[location]
    final = []
    while True:
        for j in AL_list:
            if check[j] == max(priorities):
                final.append(j)
                priorities.pop(0)
            elif check[j] != max(priorities):
                a = priorities.pop(0)
                priorities.append(a)
        answer = final.index(my)

    return answer

print(solution([2, 1, 3, 2], 2))
print(solution([1, 1, 9, 1, 1, 1], 0))




