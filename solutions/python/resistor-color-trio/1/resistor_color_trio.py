def label(colors):
    color_map = {
        "black": 0,
        "brown": 1,
        "red": 2,
        "orange": 3,
        "yellow": 4,
        "green": 5,
        "blue": 6,
        "violet": 7,
        "grey": 8,
        "white": 9,
    }

    first, second, multiplier = colors[:3]
    value = (color_map[first] * 10 + color_map[second]) * (10 ** color_map[multiplier])

    return _format_label(value)


def _format_label(value):
    if value >= 1_000_000_000:
        return f"{_format_value(value, 1_000_000_000)} gigaohms"
    if value >= 1_000_000:
        return f"{_format_value(value, 1_000_000)} megaohms"
    if value >= 1_000:
        return f"{_format_value(value, 1_000)} kiloohms"
    return f"{value} ohms"


def _format_value(value, unit):
    number = value // unit
    if value % unit == 0:
        return str(number)

    whole, remainder = divmod(value, unit)
    remainder_str = str(remainder).rjust(len(str(unit)) - 1, "0").rstrip("0")
    return f"{whole}.{remainder_str}"
