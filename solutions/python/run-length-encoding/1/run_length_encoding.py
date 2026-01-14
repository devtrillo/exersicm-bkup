def decode(string):
    result = []
    count = ""

    for char in string:
        if char.isdigit():
            count += char
            continue
        run_length = int(count) if count else 1
        result.append(char * run_length)
        count = ""

    return "".join(result)


def encode(string):
    if not string:
        return ""

    result = []
    current = string[0]
    count = 1

    for char in string[1:]:
        if char == current:
            count += 1
            continue
        if count == 1:
            result.append(current)
        else:
            result.append(f"{count}{current}")
        current = char
        count = 1

    if count == 1:
        result.append(current)
    else:
        result.append(f"{count}{current}")

    return "".join(result)
