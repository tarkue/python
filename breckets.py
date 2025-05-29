end_brackets = {
    '[': ']',
    '{': '}',
    '(': ')'
}

def is_valid_parentheses(s):
    stack = []
    for char in s:
        if char in end_brackets:
            stack.append(char)
        elif char == end_brackets[stack[-1]]:
            if not stack:
                return False
            stack.pop()
    return not stack
