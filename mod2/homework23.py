'''
Homework23
Name: "Travis Routhier"
github link:"https://github.com/Tarsum67/Python"
'''


def group_by_first_letter(words):
    grouped_words = {}

    for word in words:
        if word:
            first_letter = word[0].lower()
            if first_letter not in grouped_words:
                grouped_words[first_letter] = []
            grouped_words[first_letter].append(word)

    return grouped_words


def convert_to_sentence(words):
    if not words:  # Handle empty list case
        return ""
    return " ".join(words) + "."
       


if __name__ == "__main__":
    import doctest
    print(doctest.testfile('doctest23.py'))
