# def fionacci(n):
#     if n == 1:
#         return 1
#     elif n == 2:
#         return 2
    
#     answer = fionacci(n-1) + fionacci(n-2)
    
#     return answer

# def solution(n):
    
#     answer = fionacci(n)
#     return answer

def solution(n):
    if n <= 2:
        return n

    prev1, prev2 = 1, 2
    for _ in range(3, n + 1):
        current = (prev1 + prev2) % 1234567
        prev1, prev2 = prev2, current

    return prev2