'''
Homework22
Name: "Travis Routhier"
github link:"https://github.com/Tarsum67/Python"
'''


def mask_creditcard(string):
    return '*' * (len(string) - 4) + string[-4:]
 



def remove_vowels(string):
    vowels = "aeiouAEIOU"
    for char in vowels:
        string = string.replace(char, '')
    return string
  


if __name__ == "__main__":
    import doctest
    print(doctest.testfile('doctest22.py'))
