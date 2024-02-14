def solution(price, money, count):
    answer = -1
    
    sum_of_count = sum(range(1, count+1))
    answer = price*sum_of_count-money
    
    if answer < 0:
        return 0
    else:
        return answer