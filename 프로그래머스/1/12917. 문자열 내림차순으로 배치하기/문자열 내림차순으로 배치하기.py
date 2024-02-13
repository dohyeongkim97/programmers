def solution(s):
    answer = ''
    large = []
    small = []
    for alpha in s:
        if alpha in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
            large.append(alpha)
        
        else:
            small.append(alpha)
            
    large = ''.join(sorted(large, reverse=True))
    small = ''.join(sorted(small, reverse=True))
    answer = small+large
        
    return answer