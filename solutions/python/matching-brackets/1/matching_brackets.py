def is_paired(input_string):
    pairs = {")": "(", "]": "[", "}": "{"}
    stack = []
    for char in input_string:
        if char in pairs.values():
            stack.append(char)
        elif char in pairs:
            if not stack or stack[-1] != pairs[char]:
                return False
            stack.pop()
    return not stack
