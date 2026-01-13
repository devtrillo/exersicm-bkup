def distance(strand_a, strand_b):
    if len(strand_a) != len(strand_b):
        raise ValueError("Strands must be of equal length.")

    differences = 0
    for left, right in zip(strand_a, strand_b):
        if left != right:
            differences += 1
    return differences
