"""
Group Name: Group 9

Group Members:

Janelle Dobunaba - ######
Kien Nguyen - 400447
TJ Woods - 402983
Andrew Yang - ######

See README.md for how to input and where to find output
"""


def task1(text) -> str:
    """Character Census"""
    report = ""

    return report


def task2(text) -> str:
    """Case and Vowel Breakdown"""
    report = ""

    return report


def task3(text) -> str:
    """Word Statistics"""
    report = ""

    return report


def task4(text) -> str:
    """Line and Sentence Analysis"""
    report = ""

    return report


if __name__ == "__main__":
    # Get input
    with open("input.txt", "r") as inpt:
        text = inpt.read()

    # Create Report
    report = ""

    report += task1(text) + "\n----------------------\n"
    report += task2(text) + "\n----------------------\n"
    report += task3(text) + "\n----------------------\n"
    report += task4(text) + "\n----------------------\n"

    # Write Report
    with open("output.txt", "w") as outpt:
        outpt.write(report)
    print("Report written into `output.txt`")
