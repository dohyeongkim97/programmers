def is_valid(s):
    stack = []
    for char in s:
        if char in "([{":
            stack.append(char)
        elif char in ")]}":
            if not stack:
                return False
            elif char == ")" and stack[-1] == "(":
                stack.pop()
            elif char == "]" and stack[-1] == "[":
                stack.pop()
            elif char == "}" and stack[-1] == "{":
                stack.pop()
            else:
                return False
    return not stack

def solution(s):
    answer = 0
    n = len(s)
    for i in range(n):
        rotated_s = s[i:] + s[:i]
        if is_valid(rotated_s):
            answer += 1
    return answer