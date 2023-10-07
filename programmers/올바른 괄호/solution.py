// [문제 링크]: https://school.programmers.co.kr/learn/courses/30/lessons/12909

def solution(s):
    
    total = 0
    
    for i in s:
        if i == '(':
            total += 1
        else:
            total -= 1
        
        if total < 0:
            return False
        
    if total == 0:
        return True
    
    else :
        return False
