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
    words = []
    current_word = ""
    
    for character in text:
        if character.isalpha() or character == "'":
            current_word += character
        else:
            if current_word != "":
                words.append(current_word)
                current_word = ""
    
    if current_word != "":
        words.append(current_word)
    
    total_words = len(words)
    
    longest_word = ""
    longest_length = 0
    total_length = 0
    
    for word in words:
        word_len = len(word)
        total_length += word_len
        if word_len > longest_length:
            longest_length = word_len
            longest_word = word
    
    if total_words > 0:
        average_length = round(total_length / total_words, 1)
    else:
        average_length = 0.0

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
