def commands(binary_str):
    bits = binary_str.zfill(5)
    actions = []
    mapping = ["wink", "double blink", "close your eyes", "jump"]
    for index, action in enumerate(mapping):
        if bits[-1 - index] == "1":
            actions.append(action)
    if bits[-5] == "1":
        actions.reverse()
    return actions
