// [문제 링크]: https://school.programmers.co.kr/learn/courses/30/lessons/42842

def solution(brown, yellow):
    answer = []
    
    x = 1
    
    while True:
        y = yellow/x
        
        if (brown + yellow) == (x+2)*(y+2):
            if x > y:
                answer = [x+2, y+2]
                
            else:
                answer = [y+2, x+2]
            break
            
        else:
            x += 1
                
    
    return answer