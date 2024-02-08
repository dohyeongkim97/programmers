from itertools import combinations

def solution(elements):
    
    len_elem = len(elements)
    
    elements.extend(elements)
    
    sums = []
    i = 0
    while i < len_elem:
        j = 0
        while j < len_elem:
            sums.append(sum(elements[i:i+j]))
            j += 1
        i += 1
            
    answer = len(set(sums))
    
    return answer