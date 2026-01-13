def rebase(input_base, digits, output_base):
    if input_base < 2:
        raise ValueError("input base must be >= 2")
    if output_base < 2:
        raise ValueError("output base must be >= 2")

    value = 0
    if not digits:
        return [0]

    for digit in digits:
        if digit < 0 or digit >= input_base:
            raise ValueError("all digits must satisfy 0 <= d < input base")
        value = value * input_base + digit

    if value == 0:
        return [0]

    output_digits = []
    while value > 0:
        value, remainder = divmod(value, output_base)
        output_digits.append(remainder)

    return list(reversed(output_digits))
