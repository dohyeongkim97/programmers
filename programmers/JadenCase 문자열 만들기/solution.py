// [문제 링크]: https://school.programmers.co.kr/learn/courses/30/lessons/12951

def solution(s):
    
    answer = str()
    
    sl = list(s.split(' '))
    
    try : int(sl[0][0])
    
    except : answer += sl[0].capitalize()
    
    else: answer += sl[0][0]+sl[0][1:].lower()
    
    for i in range(1, len(sl)):
        try: int(sl[i][0])
        
        except:
            if sl[i] == ' ':
                answer += sl[i]
            else:
                answer += ' '
                answer += sl[i].capitalize()
                
        else:
            if sl[i] == ' ':
                answer += sl[i]
            else:
                answer += ' '
                answer += sl[i][0]
                answer += sl[i][1:].lower()
    
    return answer