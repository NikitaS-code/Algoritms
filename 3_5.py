def is_valid_bracket_sequence(s: str) -> str:
    stack = []
    matching = {')': '(', ']': '[', '}': '{'}

    for char in s:
        if char in '([{':
            stack.append(char)
        elif char in ')]}':
            if not stack or stack[-1] != matching[char]:
                return 'no'
            stack.pop()

    return 'yes' if not stack else 'no'

if __name__ == "__main__":
    s = input().strip()
    print(is_valid_bracket_sequence(s))
