// [문제 링크]: https://school.programmers.co.kr/learn/courses/30/lessons/120819

def solution(money):
    answer = [0, 0]
    
    answer[0] = money//5500
    answer[1] = money%5500
    return answer