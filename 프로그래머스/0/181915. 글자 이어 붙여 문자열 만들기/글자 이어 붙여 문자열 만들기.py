def solution(my_string, index_list):
    answer = ' '
    for i in range(max(index_list) + len(index_list)):
        answer += ' '
    answer = list(answer)
    for i in range(len(index_list)):
        answer[i] = my_string[index_list[i]]
        
    answer = ''.join(answer)
    answer = answer.replace(' ', '')
    return answer