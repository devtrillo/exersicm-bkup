def rotate(text, key):
    result = []
    shift = key % 26
    for char in text:
        if "a" <= char <= "z":
            offset = ord(char) - ord("a")
            result.append(chr(ord("a") + (offset + shift) % 26))
        elif "A" <= char <= "Z":
            offset = ord(char) - ord("A")
            result.append(chr(ord("A") + (offset + shift) % 26))
        else:
            result.append(char)
    return "".join(result)
