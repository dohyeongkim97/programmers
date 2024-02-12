def solution(num_list):
    answer = 0
    
    if min(num_list) > 0:
        return -1
    for i in range(len(num_list)):
        if num_list[i]<0:
            return i
    return answer