// [문제 링크]: https://school.programmers.co.kr/learn/courses/30/lessons/120903

def solution(s1, s2):
    answer = 0
    
    set1 = set(s1)
    set2 = set(s2)
    
    answer = len(set1&set2)
    return answer