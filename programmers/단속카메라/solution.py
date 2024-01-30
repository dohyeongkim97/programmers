// [문제 링크]: https://school.programmers.co.kr/learn/courses/30/lessons/42884

def solution(routes):
    answer = 1
    
    routes.sort(key=lambda x: x[1])
    
    now = routes[0][1]
    for i in range(len(routes)):
        if now < routes[i][0]:
            now = routes[i][1]
            answer += 1
    return answer