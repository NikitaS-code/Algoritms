def evaluate_postfix(expression: str) -> int:
    tokens = expression.strip().split()
    stack = []

    for token in tokens:
        if token.isdigit() or (token[0] == '-' and token[1:].isdigit()):
            stack.append(int(token))
        else:
            b = stack.pop()
            a = stack.pop()

            if token == '+':
                stack.append(a + b)
            elif token == '-':
                stack.append(a - b)
            elif token == '*':
                stack.append(a * b)

    return stack[0]


if __name__ == "__main__":
    expr = input()
    print(evaluate_postfix(expr))
