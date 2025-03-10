'''
Homework20
Name: "Travis Routhier"
github link:"https://github.com/Tarsum67/Python"
'''


def convert_to_ascii(string):
    return ord(string) if len(string) == 1 else [ord(char) for char in string]



def filter_non_ascii(string):
    print(''.join(char for char in string if ord(char) < 128))


if __name__ == "__main__":
    import doctest
    print(doctest.testfile('doctest20.py'))
