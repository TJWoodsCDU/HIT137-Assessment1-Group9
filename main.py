"""
Group Name: Group 9

Group Members:

Janelle Dobunaba - ######
Kien Nguyen - 400447
TJ Woods - 402983
Yucheng Yang - 394389

See README.md for how to input and where to find output
"""


def task1(text) -> str:
    """Character Census"""

    num_chars = 0
    num_letters = 0
    num_numbers = 0
    num_whitespace = 0
    num_other = 0
    for char in text:
        # 1. Number of characters
        num_chars += 1

        # 2. Number of letters
        if char.isalpha():
            num_letters += 1

        # 3. Number of numbers
        elif char.isdigit():
            num_numbers += 1

        # 4. Number of whitespace characters
        elif char in " \t\n":
            num_whitespace += 1

        # 5. Number of other characters (punctuation and so on)
        else:
            num_other += 1
    # Check
    assert (
        num_letters +
        num_numbers +
        num_whitespace +
        num_other
        ) == num_chars, "Error in task1: character count mismatch"

    # Format report
    report = f"""
    Task 1: Character Census

    Total number of characters: {num_chars},
    Number of letters: {num_letters},
    Number of numbers: {num_numbers},
    Number of whitespace characters: {num_whitespace},
    Number of other characters: {num_other}
    """

    return report


def task2(text) -> str:
    """Case and Vowel Breakdown"""

    upper_count = 0
    lower_count = 0
    total_vowels = 0
    total_consonants = 0
    vowel_a = 0
    vowel_e = 0
    vowel_i = 0
    vowel_o = 0
    vowel_u = 0
    vowels = "aeiou"

    for char in text:
        if char.isalpha():
            # Count upper / lower case
            if char.isupper():
                upper_count += 1
            else:
                lower_count += 1

           lower_char = char.lower()
            if lower_char in vowels:
                total_vowels += 1
                # Count each single vowel
                if lower_char == "a":
                    vowel_a += 1
                elif lower_char == "e":
                    vowel_e += 1
                elif lower_char == "i":
                    vowel_i += 1
                elif lower_char == "o":
                    vowel_o += 1
                elif lower_char == "u":
                    vowel_u += 1
         else:
            total_consonants += 1
  
    # Format report                   
    report = f"""
    Task 2: Case and Vowel Breakdown

    Uppercase letters: {upper_count},
    Lowercase letters: {lower_count},
    Total vowels: {total_vowels},
    Individual vowel counts:
        a: {vowel_a},  e: {vowel_e},  i: {vowel_i},  o: {vowel_o},  u: {vowel_u},
    """
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

    # Format report
    report = f"""
    Task 3: Word Statistics

    Total number of words: {total_words},
    Longest word: {longest_word},
    Longest word length: {longest_length} characters,
    Average word length: {average_length} characters
    """

    return report


def task4(text) -> str:
    """Line and Sentence Analysis"""

    # Initialise variables
    num_lines = 0
    num_sentences = 0
    len_long_line = 0
    line_lengths = [0]
    i = 0

    # Scan text
    for char in text:
        # 1. Number of lines
        if char == "\n":
            num_lines += 1

        # 2. Number of sentences
        if char in ".!?":
            num_sentences += 1

        # 3. Length of longest line
        if char == "\n":  # This condition is only repeated for task separation / clarity
            line_lengths.append(0)
            i += 1
        else:
            line_lengths[i] += 1
    len_long_line = max(line_lengths)

    # Format report
    report = f"""
    Task 4: Line and Sentence Analysis

    Number of lines: {num_lines},
    Number of sentences: {num_sentences},
    Length of longest line: {len_long_line}
    """

    return report


def format_report(report) -> str:
    report = report.lstrip().rstrip() + "\n\n--------------------\n\n"
    return report


if __name__ == "__main__":
    # Get input
    with open("input.txt", "r") as inpt:
        text = inpt.read()

    # Create report
    report = ""

    report += format_report(task1(text))
    report += format_report(task2(text))
    report += format_report(task3(text))
    report += format_report(task4(text))

    report = report.rstrip()

    # Write report
    with open("output.txt", "w") as outpt:
        outpt.write(report)
    print("Report written into `output.txt`")
