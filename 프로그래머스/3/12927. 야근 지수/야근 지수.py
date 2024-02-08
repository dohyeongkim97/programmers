def solution(n, works):
    answer = 0
    
    max_time = max(works)
    while (n > 0) and (max_time)>0:
        for i in range(len(works)):
            if works[i] == max_time:
                if n > 0:
                    n -= 1
                    works[i] = works[i]-1
                else:
                    break
                
        max_time -= 1
    
    for i in works:
        answer += i**2
    return answer