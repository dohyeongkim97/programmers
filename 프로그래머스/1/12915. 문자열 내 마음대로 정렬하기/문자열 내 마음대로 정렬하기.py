def solution(strings, n):
    answer = []

    dicts = {
        
    }
    
    for i in 'abcdefghijklmnopqrstuvwxyz':
        dicts[i] = []
        
    for char in strings:
        dicts[char[n]].append(char)
        
    for i in 'abcdefghijklmnopqrstuvwxyz':
        for alf in sorted(dicts[i]):
            answer.append(alf)

    return answer