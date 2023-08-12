// [문제 링크]: https://school.programmers.co.kr/learn/courses/30/lessons/42862

def solution(n, lost, reserve):
    answer = 0
    students = [1] * n  # 초기값을 1로 설정 (체육복 여분 있는 상태)
    
    for i in lost:
        students[i-1] -= 1
        
    for i in reserve:
        students[i-1] += 1
        
    for i in range(n):
        if students[i] == 0:
            if i > 0 and students[i-1] == 2:
                students[i] += 1
                students[i-1] -= 1
            elif i < n-1 and students[i+1] == 2:
                students[i] += 1
                students[i+1] -= 1
                
    answer = sum(1 for s in students if s > 0)
    
    return answer