// [문제 링크]: https://school.programmers.co.kr/learn/courses/30/lessons/120889

def solution(sides):
    answer = 0
    
    if max(sides) >= sum(sides)-sides[sides.index(max(sides))]:
        return 2
    else:
        return 1
    return answer