'''
Homework8
Name: "Travis Routhier"
github link:"https://github.com/Tarsum67/Python"
'''

def sum_numbers(lst):
    # your code here
    sum = 0
    for i in lst:
        sum += i
    return sum

def largest_number(lst):
    # your code here
    lst.sort()
    return lst[-1]
  

if __name__ == "__main__":
    import doctest
    print(doctest.testfile('doctest8.py'))
