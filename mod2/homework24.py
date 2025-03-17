'''
Homework24
Name: "Travis Routhier"
github link: https://github.com/Tarsum67/Python/tree/main/mod2/homework24.py
'''


def isBetween(word):
    if len(word) < 8 or len(word) > 20:
        return False
    else:
        return True


def isUpper(word):
    for i in word:
        if i.isupper():
            return True
    return False


def isLower(word):
    for i in word:
        if i.islower():
            return True
    return False


def isDigit(word):
    for i in word:
        if i.isdigit():
            return True
    return False


def isSpecial(word):
    special = "!@#$%^&*()-+"
    for i in word:
        if i in special:
            return True
    return False


def is_valid_password(word):
    if isBetween(word) and isUpper(word) and isLower(word) and isDigit(word) and isSpecial(word):
        return True
    else:
        return False


if __name__ == "__main__":
    import doctest
    print(doctest.testfile('doctest24.py'))
