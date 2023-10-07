// [문제 링크]: https://school.programmers.co.kr/learn/courses/30/lessons/12911

def solution(n):
    answer = 0
    
    i = 1
    while n < 100000000:
        num = bin(n+i)
        
        number = 0
        for j in num:
            if j== '1':
                number+=1

        number2 = 0
        num2 = bin(n)
        for j in num2:
            if j== '1':
                number2 += 1
                
        if number == number2:
            answer = (n+i)
            break
            
        else:
            i += 1
    
    return answer