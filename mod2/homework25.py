'''
Homework24
Name: Travis Routhier
github link: https://github.com/Tarsum67/Python/tree/main/mod2/homework25.py
'''


def flowers(idx, list_of_flowers):
    try:
        idx = int(idx)
        print(f"You selected: {list_of_flowers[idx]}")
    except ValueError:
        print("Invalid input! Please enter a number.")
    except IndexError:
        print("Number out of range! Please choose a valid flower number.")


if __name__ == "__main__":
    import doctest
    print(doctest.testfile('doctest25.py'))
