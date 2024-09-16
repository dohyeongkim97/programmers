def solution(wallet, bill):
    answer = 0
    
    while True:
        if (max(bill) <= max(wallet)) and (min(bill) <= min(wallet)):
            return answer
        else:
            bill = [min(bill), max(bill)//2]
            answer += 1
    
    
    return answer