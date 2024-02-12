def solution(n):
    answer = ''
    n = str(n)
    sorted_n = sorted(n, reverse=True)
    sorted_n = ''.join(sorted_n)
    answer = int(sorted_n)
    return answer