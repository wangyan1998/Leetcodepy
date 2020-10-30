# 判断一个只包含括号的字符串是否合法，括号包含()[]{}
def isValid(s: str) -> bool:
    if len(s) % 2 == 1:
        return False

    paris = {")": "(", "]": "[", "}": "{", }
    stack = list()
    for ch in s:
        if ch in paris:
            if not stack or stack[-1] != paris[ch]:
                return False
            else:
                stack.append(ch)

    return not stack
