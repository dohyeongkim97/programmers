// [문제 링크]: https://school.programmers.co.kr/learn/courses/30/lessons/12945

def solution(n):
    
    def fs_loop(n):
    
        if n == 1:
            return 0
        if n == 2:
            return 1

        first = 0

        second = 1

        i = 1
        while i <= n - 1:
            first += second
            second += first
            i += 2

        if n % 2:
            return second
        else:
            return first
    
    answer = fs_loop(n) % 1234567
    
    return answer