def abbreviate(words):
    import re

    tokens = re.findall(r"[A-Za-z]+(?:'[A-Za-z]+)*", words)
    return "".join(token[0].upper() for token in tokens)
