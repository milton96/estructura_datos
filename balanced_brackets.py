def is_balanced(s: str) -> str:
    if len(s) == 1:
        return False
    stack = []
    for b in s:
        if b in "{[(":
            stack.append(b)
        else:
            if len(stack) > 0:
                if b == "}" and stack[-1] == "{":
                    stack.pop()
                elif b == "]" and stack[-1] == "[":
                    stack.pop()
                elif b == ")" and stack[-1] == "(":
                    stack.pop()
                else:
                    stack.append(b)
            else:
                stack.append(b)

    return "SI" if len(stack) == 0 else "NO"

def is_balanced_v2(s: str) -> bool:
    stack = []
    d = {'{': '}', '[': ']', '(': ')'}
    for i in s:
        if i in d:
            stack.append(i)
        elif len(stack) == 0 or d[stack.pop()] != i:
            return False
    return len(stack) == 0

if __name__ == "__main__":
    s1 = ")(){}"

    print(is_balanced(s1))
    print(is_balanced_v2(s1))