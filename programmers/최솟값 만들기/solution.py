// [문제 링크]: https://school.programmers.co.kr/learn/courses/30/lessons/12941

def solution(A,B):
    answer = 0
    
    list_a = sorted(A)
    list_b = sorted(B, reverse=True)

    answer = 0
    for i in range(len(list_a)):
        answer += list_a[i] * list_b[i]

    return answer