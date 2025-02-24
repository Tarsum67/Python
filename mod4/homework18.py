'''
Homework18
Name: "Travis Routhier"
github link:"https://github.com/Tarsum67/Python" 
'''

def iterate_dictionary(lst):
    dict = {1:"one",2:"two",3:"three"}
    for num in lst:
        try:
            print(dict[num])
        except:
            print("Number not in dictionary")
    # your code here
    return

def check_if_positive(lst):
    # your code here
    for num in lst:
        if num > 0:
            print(num)
        else:
            print("not positive")
    return

def division(lst):
    # your code here
    for num in lst:
        try:
            print(round(100/num,2))
        except:
            print("can't divide by zero")
    return 

if __name__ == "__main__":
    import doctest
    print(doctest.testfile('doctest18.py'))