def solution(n):
    answer = 0
    n_string = []
    
    while n > 2:
        n_string.append(str(int(n%3)))
        n = (n-n%3)/3

    n_string.append(str(int(n)))
    n_string = ''.join(n_string)
    n_string = n_string[::-1]
    print(n_string)
    

    for i in range(len(n_string)):
        answer += int(n_string[i])*(3**i)
    return answer
