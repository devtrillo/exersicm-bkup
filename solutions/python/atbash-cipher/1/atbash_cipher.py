def encode(plain_text):
    normalized = []
    for char in plain_text.lower():
        if char.isalnum():
            normalized.append(char)

    encoded = _translate("".join(normalized))
    grouped = []
    for index, char in enumerate(encoded):
        if index and index % 5 == 0:
            grouped.append(" ")
        grouped.append(char)
    return "".join(grouped)


def decode(ciphered_text):
    normalized = []
    for char in ciphered_text.lower():
        if char.isalnum():
            normalized.append(char)
    return _translate("".join(normalized))


def _translate(text):
    translated = []
    for char in text:
        if char.isalpha():
            offset = ord(char) - ord("a")
            translated.append(chr(ord("z") - offset))
        else:
            translated.append(char)
    return "".join(translated)
