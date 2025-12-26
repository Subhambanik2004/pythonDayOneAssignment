def validate_roll(roll):
    return roll > 0


def grade(avg):
    if avg >= 75:
        return "A"
    elif avg >= 60:
        return "B"
    else:
        return "C"
