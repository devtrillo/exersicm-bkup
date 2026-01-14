def prime(number):
    if number <= 0:
        raise ValueError("there is no zeroth prime")

    if number <= 5:
        return [2, 3, 5, 7, 11][number - 1]

    import math

    def nth_prime_with_limit(limit):
        sieve = [True] * (limit + 1)
        sieve[0:2] = [False, False]
        for candidate in range(2, int(limit**0.5) + 1):
            if sieve[candidate]:
                sieve[candidate * candidate : limit + 1 : candidate] = [False] * (
                    ((limit - candidate * candidate) // candidate) + 1
                )
        primes = [idx for idx, is_prime in enumerate(sieve) if is_prime]
        if len(primes) >= number:
            return primes[number - 1]
        return None

    limit = int(number * (math.log(number) + math.log(math.log(number)))) + 3
    while True:
        result = nth_prime_with_limit(limit)
        if result is not None:
            return result
        limit *= 2
