def classify(number):
    """A perfect number equals the sum of its positive divisors.

    :param number: int a positive integer
    :return: str the classification of the input integer
    """
    if number <= 0:
        raise ValueError("Classification is only possible for positive integers.")

    if number == 1:
        return "deficient"

    divisors_sum = 1
    limit = int(number**0.5)
    for divisor in range(2, limit + 1):
        if number % divisor == 0:
            divisors_sum += divisor
            paired = number // divisor
            if paired != divisor:
                divisors_sum += paired

    if divisors_sum == number:
        return "perfect"
    if divisors_sum > number:
        return "abundant"
    return "deficient"
