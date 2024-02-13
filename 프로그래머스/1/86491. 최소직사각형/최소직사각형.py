def solution(sizes):
    for i in sizes:
        if i[0] < i[1]:
            temp = i[0]
            i[0] = i[1]
            i[1] = temp
        else:
            continue
        
    height = []
    width = []
    
    for i in sizes:
        height.append(i[0])
        width.append(i[1])
        
    answer = max(height) * max(width)
    return answer