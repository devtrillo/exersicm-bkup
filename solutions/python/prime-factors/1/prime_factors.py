def factors(value):
    remaining = value
    result = []
    divisor = 2

    while divisor * divisor <= remaining:
        while remaining % divisor == 0:
            result.append(divisor)
            remaining //= divisor
        divisor = 3 if divisor == 2 else divisor + 2

    if remaining > 1:
        result.append(remaining)

    return result
