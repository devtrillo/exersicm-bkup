def resistor_label(colors):
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
    tolerance_map = {
        "grey": "0.05%",
        "violet": "0.1%",
        "blue": "0.25%",
        "green": "0.5%",
        "brown": "1%",
        "red": "2%",
        "gold": "5%",
        "silver": "10%",
    }

    if len(colors) == 1:
        return "0 ohms"

    if len(colors) == 4:
        significant_colors = colors[:2]
        multiplier_color = colors[2]
        tolerance_color = colors[3]
    else:
        significant_colors = colors[:3]
        multiplier_color = colors[3]
        tolerance_color = colors[4]

    significant = 0
    for color in significant_colors:
        significant = significant * 10 + color_map[color]

    multiplier = 10 ** color_map[multiplier_color]
    value = significant * multiplier

    resistance = _format_label(value)
    return f"{resistance} \u00b1{tolerance_map[tolerance_color]}"


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
