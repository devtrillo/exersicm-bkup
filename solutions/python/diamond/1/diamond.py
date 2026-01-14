def rows(letter):
    size = ord(letter) - ord("A")
    width = size * 2 + 1
    result = []

    for idx in range(size + 1):
        char = chr(ord("A") + idx)
        if idx == 0:
            line = char
        else:
            inner = " " * (idx * 2 - 1)
            line = f"{char}{inner}{char}"
        outer = " " * (size - idx)
        result.append(f"{outer}{line}{outer}")

    return result + result[-2::-1]
