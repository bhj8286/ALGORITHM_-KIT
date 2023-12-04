# 내 풀이 
def solution(s):
    if s[0] == ')':
        answer = False
    else:
        check = []
        checheck = []
        for i in s:
            if i == '(':
                check.append(i)
            elif i == ')':
                checheck.append(i)
                #  "())((()))(()" 같은 경우는 올바르지 않은데도 최종 괄호의 합이 같아 True가 나온다. 따라서 도중에 checheck의 리스트 길이가 더 길면 False를 반환하도록 함.
                if len(checheck) > len(check): 
                    answer = False
                    break
        if len(checheck) == len(check):
            answer = True
        else: 
            answer =False


    return answer

print(solution("()()"))
print(solution("(())()"))
print(solution(")()("))
print(solution("(()("))