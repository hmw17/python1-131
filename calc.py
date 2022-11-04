import math
def calculator(in_str):
    in_str = in_str.replace(" ", "")
    legal_input = ['+', '-', '*', '/', '(', ')']
    # res:return value
    res = 0
    stack = []
    num = 0
    sign = '+'
    i = 0
    while i < len(in_str):
        if in_str[i] >= '0' and in_str[i] <= '9':
            num = num * 10 + int(in_str[i])
        elif in_str[i] not in legal_input:
            raise RuntimeError("illegal input")
        if in_str[i] == '(':
            left = i
            parentheses_cnt = 1
            i += 1
            if in_str[i] == ')':
                raise RuntimeError("illegal parentheses")
            while parentheses_cnt > 0:
                if in_str[i] == '(':
                    parentheses_cnt += 1
                elif in_str[i] == ')':
                    parentheses_cnt -= 1
                i += 1
            num = calculator(in_str[left + 1:i - 1])
            i -= 1

        tmpSign = sign
        if in_str[i] == '+':
            tmpSign = '+'
        elif in_str[i] == '-':
            tmpSign = '-'
        elif in_str[i] == '*':
            if in_str[i + 1] != '*':
                tmpSign = '*'
            else:
                i += 1
                tmpSign = '**'
        elif in_str[i] == '/':
            if in_str[i + 1] != '/':
                tmpSign = '/'
            else:
                i += 1
                tmpSign = '//'

        if i == len(in_str) - 1 or in_str[i] in ["+", "-", "*", "/"]:
            if sign == '+':
                stack.append(num)
            elif sign == '-':
                stack.append(-num)
            elif sign == '*':
                stack[-1] *= num
            elif sign == '**':
                stack[-1] = math.pow(stack[-1], num)
            elif sign == '/':
                if num == 0:
                    raise RuntimeError("divide 0")
                stack[-1] /= num
            elif sign == '//':
                if num == 0:
                    raise RuntimeError("divide 0")
                stack[-1] = stack[-1] // num
            sign = tmpSign
            num = 0
        i += 1
    while stack:
        res += stack.pop()
    return float(res)