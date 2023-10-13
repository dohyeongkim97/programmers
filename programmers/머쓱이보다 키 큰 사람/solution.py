// [문제 링크]: https://school.programmers.co.kr/learn/courses/30/lessons/120585

def solution(array, height):
    answer = 0
    array = sorted(array)
    
    for i in range(len(array)):
        if array[i] > height:
            return len(array)-i
    return 0