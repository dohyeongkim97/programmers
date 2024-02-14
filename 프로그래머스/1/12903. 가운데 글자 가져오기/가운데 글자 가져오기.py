def solution(s):
    answer = ''
    if len(s):
        answer = s[(len(s)/2)-1]
    else:
        answer = s[len(s)/2-1:len(s)/2+1]
    return answer