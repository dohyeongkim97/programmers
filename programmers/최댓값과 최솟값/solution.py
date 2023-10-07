// [문제 링크]: https://school.programmers.co.kr/learn/courses/30/lessons/12939

def solution(s):
    lst = list(s.split(' '))
    max_num = int(lst[0])
    min_num = int(lst[0])
    i = 0
    while i < len(lst):
        if int(lst[i]) > max_num:
            max_num = int(lst[i])
            
        if int(lst[i]) < min_num:
            min_num = int(lst[i])
        
        i += 1
            
    answer = "{0} {1}".format(min_num, max_num)
    return answer