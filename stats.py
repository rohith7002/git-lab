"""Statistics for a list of marks."""


def average(marks):
    if not marks:
        return 0
    return sum(marks) / len(marks)


def highest(marks):
    if not marks:
        return 0
    return max(marks)


def lowest(marks):
    if not marks:
        return 0
    return min(marks)


def pass_count(marks, pass_mark):
    return len([mark for mark in marks if mark >= pass_mark])
