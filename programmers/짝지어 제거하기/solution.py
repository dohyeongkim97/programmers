// [문제 링크]: https://school.programmers.co.kr/learn/courses/30/lessons/12973

def solution(s):
    stack = []
    
    for c in s:
        if stack and stack[-1] == c:
            stack.pop() 
        else:
            stack.append(c)  
    
    if not stack:
        answer = 1
    else:
        answer = 0
        
    return answer