'''
Homework24
Name: Travis Routhier
github link: https://github.com/Tarsum67/Python/tree/main/mod2/homework26.py
'''


def dictionary_exceptions(key, dict):
    try:
        price = dict[key]
        print(f"The price of {key} is ${price}")
    except KeyError:
        print("Error: Flower not found! Please enter Rose, Lily, or Tulip.")


def string_exceptions(idx, str):
    try:
        idx = int(idx)
        print(f"The character at index {idx} is: {str[idx]}")
    except ValueError:
        print("Error: String indices must be integers, not 'str'")
    except IndexError:
        print("Error: Index out of range! Please enter a valid index.")
    except TypeError as e:
        print(
            f"Error: String indices must be integers, not '{type(idx).__name__}' ")


if __name__ == "__main__":
    import doctest
    print(doctest.testfile('doctest26.py'))
