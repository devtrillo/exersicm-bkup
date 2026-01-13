def square_root(number):
    candidate = 0
    while candidate * candidate < number:
        candidate += 1
    return candidate
