def solution(n, s):
    
    if n>s:
        answer = [-1]
        return answer
        
    answer = [(s//n) for _ in range(n)]
    
    elses = s - (s//n)*n
    
    i = 0
    while elses>0:
        answer[n-i-1] += 1
        elses -= 1
        i += 1

    
    return answer