# 같은 자리에 있는 수들을 비교해서 큰 것부터 배치하면 된다
# def solution(numbers):
#     answer = ''
#     string_numbers = list(map(str, numbers))
#     my = dict(zip(string_numbers, numbers))
#     for i in string_numbers:
        
#     return answer

# print(solution([6, 10, 2]))
# print(solution([3, 30, 34, 5, 9]))

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


print(solution([1000, 100])) # 반례
print(solution([6, 10, 2]))
print(solution([3, 30, 34, 5, 9]))
