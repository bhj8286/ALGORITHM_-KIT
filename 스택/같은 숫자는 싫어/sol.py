# 내 풀이
def solution(arr):
    answer = []
    for  i in arr:
        if len(answer) == 0:
            answer.append(i)
        elif len(answer) != 0:
            if answer[-1] != i:
                answer.append(i)
            else:
                continue
    return answer

print(solution([1,1,3,3,0,1,1]))
print(solution([4,4,4,3,3]))


# 다른 사람 비슷한 코드
def no_continuous(s):
    a = []
    for i in s:
        if a[-1:] == [i]: continue # a[-1:]은 마지막 원소를 꺼내 리스트로 만들어 준 거라 i에 리스트를 씌워야한다
        a.append(i)
    return a