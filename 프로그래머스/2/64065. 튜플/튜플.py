def solution(s):
    s = s.replace('{', '')

    s = s.replace('}}', '')

    s = s.split('},')
    
    series = [[] for _ in range(len(s))]
    
    for i in s:
        series[len(i.split(','))-1] = i
        
    answer = []
    
    nums = []

    for numbers in series:
        numbers = numbers.split(',')
        
        for num in numbers:
            if int(num) not in nums:
                nums.append(int(num))
            else:
                continue
                
    return nums
    
    return series