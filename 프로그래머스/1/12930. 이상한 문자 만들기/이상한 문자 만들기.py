# def solution(s):
#     a = s.split()
#     b = []

#     for i in a:
#         i = i.replace(' ', '')
#     for word in a:
#         c = ''
#         for i in range(len(word)):
#             if i % 2 == 0:
#                 c += word[i].upper()
#             else:
#                 c += word[i].lower()
#         b.append(c)

#     answer = ' '.join(b)
#     return answer

def solution(s):
    answer = ''
    new_list = s.split(' ')
    for i in new_list:
        for j in range(len(i)):
            if j % 2 == 0:
                answer += i[j].upper()
            else:
                answer += i[j].lower()
        answer+= ' '
    return answer[0:-1]