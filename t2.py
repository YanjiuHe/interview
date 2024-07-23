def check_brackets(input_str):
    stack = []
    result = ""
    
    for i, char in enumerate(input_str):
        if char == '(':
            stack.append(i)
        elif char == ')':
            if stack:
                stack.pop()
            else:
                result += f"{' ' * (i-len(result))}?"
    
    for i in stack:
        result += f"{' ' * (i-len(result))}x"
    
    return result

test_cases = [
    "((IIII)))))",
    "()()()()(uuu",
    "))))UUUU(()("
]

for case in test_cases:
    print(case)
    print(check_brackets(case))
    print()