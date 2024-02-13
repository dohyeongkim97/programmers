def solution(array, commands):
    answer = []
    
    for arr in commands:
        i, j, k = arr
        answer.append(sorted(array[i-1:j])[k-1])
    return answer