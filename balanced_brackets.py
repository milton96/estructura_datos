
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

if __name__ == "__main__":
    s1 = ")(){}"

    print(is_balanced(s1))