'''
Homework5
Name: "Travis Routhier"
github link:"https://github.com/Tarsum67/Python"
'''

def collatz_conjecture(num):
    num = float(num)
    while num != 1.0:
        print(num)
        if num % 2 == 0:
            num = num / 2.0
        else:
            num = num * 3.0 + 1.0
        return num


def add_numbers(num):
    return sum(range(1, num))

if __name__ == "__main__":
    collatz_conjecture(18.0)
    import doctest
    print(doctest.testfile('doctest5.py'))