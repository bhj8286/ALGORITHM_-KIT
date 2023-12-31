# 참조 정답 코드
def solution(numbers):
    numbers = list(map(str, numbers))
    numbers.sort(key=lambda x: x * 3, reverse=True) # *3을 하는 이유: x*3을 하게 되면 [3, 310, 30] -> [333, 310310310, 303030] 이렇게 된다. 자릿수를 맞춰 비교하기 위함이고 numbers의 원소는 0 이상 1,000 이하라서 3자리만 비교하면 된다.
    return str(int(''.join(numbers)))




# 틀릴 테스트케이스가 많다는 걸 알면서 했다
def solution(arr):
    answer = ''
    n = len(arr)
    string_numbers = list(map(str, arr))

    for i in range(n):
        # 각 패스마다 리스트의 끝까지 비교하며 큰 값을 뒤로 보냄
        for j in range(0, n-i-1):
            if arr.count(0) == len(arr):
                answer = 0
            if string_numbers[j][0] < string_numbers[j+1][0]:
                string_numbers[j], string_numbers[j+1] = string_numbers[j+1], string_numbers[j]
            elif string_numbers[j][0] == string_numbers[j+1][0] and len(string_numbers[j])==len(string_numbers[j+1]):
                if string_numbers[j][-1] == '0':
                    string_numbers[j], string_numbers[j+1] = string_numbers[j+1], string_numbers[j]
                elif string_numbers[j][1] < string_numbers[j+1][1]:
                    string_numbers[j], string_numbers[j+1] = string_numbers[j+1], string_numbers[j]
            elif string_numbers[j][0] == string_numbers[j+1][0] and len(string_numbers[j]) != len(string_numbers[j+1]):
                if len(string_numbers[j]) < len(string_numbers[j+1]) and string_numbers[j+1][-1] == '0':
                    string_numbers[j], string_numbers[j+1] = string_numbers[j], string_numbers[j+1]
                elif len(string_numbers[j]) < len(string_numbers[j+1]) and string_numbers[j+1][-1] != '0':
                    string_numbers[j], string_numbers[j+1] = string_numbers[j+1], string_numbers[j]
            
    answer = ''.join(string_numbers)

    return answer


print(solution([1000, 100])) # 반례 -> 통과 못함
print(solution([6, 10, 2]))
print(solution([3, 30, 34, 5, 9]))


# permutation 활용
from itertools import permutations

def solution(arr):
    string_numbers = list(map(str, arr))
    total = []

    for perm in permutations(string_numbers, len(arr)):
        total.append(int(''.join(perm)))

    answer = str(max(total))
    return answer

print(solution([6, 10, 2]))
print(solution([3, 30, 34, 5, 9]))


