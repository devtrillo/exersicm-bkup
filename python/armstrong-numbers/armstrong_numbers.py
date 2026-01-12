def is_armstrong_number(number):
    digits = [int(digit) for digit in str(number)]
    power = len(digits)
    total = sum(digit**power for digit in digits)
    return total == number
