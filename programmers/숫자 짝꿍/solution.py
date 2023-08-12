// [문제 링크]: https://school.programmers.co.kr/learn/courses/30/lessons/131128

def solution(X, Y):
    from collections import Counter
    y = Counter(Y)
    nums = []
    answer = []
    
    for i in X:
        if i in y:
            if y[i] != 0:
                nums.append(i)
                y[i] -= 1
            
    if set(nums) == {'0'}:
        return '0'
    
    if len(set(nums)) == 0:
        return '-1'
    

    nums.sort(reverse=True)
    answer = ''.join(nums)

    return answer