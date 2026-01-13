def equilateral(sides):
    return _is_valid(sides) and sides[0] == sides[1] == sides[2]


def isosceles(sides):
    return _is_valid(sides) and (
        sides[0] == sides[1] or sides[1] == sides[2] or sides[0] == sides[2]
    )


def scalene(sides):
    return _is_valid(sides) and len(set(sides)) == 3


def _is_valid(sides):
    a, b, c = sorted(sides)
    return a > 0 and a + b > c
