def solution(lottos, win_nums):
    answer = []
    
    zeros = lottos.count(0)
    
    pre = len(set(lottos)&set(win_nums))
    
    max_num = zeros+pre
    min_num = pre

    if min_num<2:
        min_num = 1
        
    if max_num<2:
        max_num = 1
        
    result = [7-max_num, 7-min_num]
    
    return result