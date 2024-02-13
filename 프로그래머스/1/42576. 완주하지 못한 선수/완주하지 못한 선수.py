def solution(participant, completion):
    answer = ''
    part_dict = {}
    for i in participant:
        if i in part_dict.keys():
            part_dict[i] += 1
        else:
            part_dict[i] = 1
            
    for i in completion:
        part_dict[i] -= 1
        
    for i in part_dict.keys():
        if part_dict[i] != 0:
            return i
    
    return answer