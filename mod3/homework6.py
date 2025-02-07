'''
Homework6
Name: "Travis Routhier"
github link:"https://github.com/Tarsum67/Python"
'''

def div_by_seven(num):
    for i in range(1, num + 1):
        if i % 7 == 0:
            print(i)

def squares_of_numbers(num):
    # your code here
    for i in range(1, num):
        print(i**2)
    return 

if __name__ == "__main__":
    import doctest
    div_by_seven(300)
    print(doctest.testfile('doctest6.py'))