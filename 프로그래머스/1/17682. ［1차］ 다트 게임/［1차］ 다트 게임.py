def solution(dartResult):
    answer = 0
    
    now = 0
    before = 0
    
    number = ''
    for i in range(len(dartResult)):
        if dartResult[i] not in ['S', 'D', 'T', '*', '#']:
            number += dartResult[i]
            
        else:
            num = int(number)
            if (i < len(dartResult)-1) and (dartResult[i+1] not in ['*', '#']):
                number = ''
            if dartResult[i] == 'S':
                answer += before
                before = now
                now = int(num)
                
            elif dartResult[i] == 'D':
                answer += before
                before = now
                now = int(num)**2
            
            elif dartResult[i] == 'T':
                answer += before
                before = now
                now = int(num)**3
                
            elif dartResult[i] == '*':
                before *= 2
                now *= 2
            
            elif dartResult[i] == '#':
                if now >= 0:
                    now *= -1
                else:
                    now *= 2


    answer += now
    answer += before
    return answer