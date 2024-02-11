def solution(clothes):
    answer = 1
    
    clothes_dict = {
        
    }
    
    for i in clothes:
        if i[1] not in clothes_dict.keys():
            clothes_dict[i[1]] = 1
        else:
            clothes_dict[i[1]]+=1
            
    for key in clothes_dict.keys():
        answer *= clothes_dict[key]+1
    
    
    return answer-1