def solution(n, arr1, arr2):
    answer = []

    binary1 = []
    binary2 = []

    for i in arr1:
        binary1.append('0'*(n-len(bin(i)[2:]))+bin(i)[2:])

    for j in arr2:
        binary2.append('0'*(n-len(bin(j)[2:]))+bin(j)[2:])
    for i in range(len(binary1)):
        printed = ''
        for num in range(len(binary1[i])):
            if binary1[i][num] == '1' or binary2[i][num] == '1':
                printed += '#'
            else:
                printed += ' '
        answer.append(printed)
    return answer