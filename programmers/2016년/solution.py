// [문제 링크]: https://school.programmers.co.kr/learn/courses/30/lessons/12901

import datetime

def solution(a, b):
    answer = ''
    
    dates = f'2016/{a}/{b}'
    
    dates = datetime.datetime.strptime(dates, '%Y/%m/%d')
    num = dates.weekday()
    
    days_dict = {
        0 : 'MON',
        1 : 'TUE',
        2 : 'WED',
        3 : 'THU',
        4 : 'FRI',
        5 : 'SAT',
        6 : 'SUN'
    }
    
    
    return days_dict[num]