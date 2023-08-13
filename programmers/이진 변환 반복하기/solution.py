// [문제 링크]: https://school.programmers.co.kr/learn/courses/30/lessons/70129

def solution(s):
    answer = []
    transform = 0
    zeros = 0
    while s != '1':
        lena = len(s)
        s = s.replace('0', '')
        lenb = len(s)
        zeros += (lena-lenb)
        s = bin(len(s))[2:]
        transform += 1

    answer = [transform, zeros]
    return answer