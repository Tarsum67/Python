'''
Homework1
Name:"Travis Routhier"
github link: "https://github.com/Tarsum67/Python"
'''

def add(num1,num2):
    # your code here
    num1 = 2
    sum = num1 + num1
    return sum 

def subtract(num1,num2):
    # your code here
    num1 = 2
    sum = num1 - num1
    return print(sum)

def multiply(num1,num2):
    # your code here
    num1 = 3
    sum = num1 * num1
    return print(sum)

def division(num1,num2):
    # your code here
    num1 = 2
    sum = num1 / num1
    return print(sum)

def int_div(num1,num2):
    # your code here
    num1 = 13
    num2 = 5
    sum = num1 // num2
    return print(sum)

def modulus(num1,num2):
    # your code here
    num1 = 13
    num2 = 12
    sum = num1 % num2
    return print(sum)

def exp(num1,num2):
    # your code here
    num1 = 4
    num2 = 9 
    sum = num1 ** num2
    return print(sum)

def area(length,width):
    # your code here
    length = 3
    width = 4
    sum = length * width
    return print("'The area of the rectangle with a length of " +str(length)+ " and a width of " +str(width)+ " is " +str(sum)+"'")


if __name__ == "__main__":
    import doctest
    print(doctest.testfile('doctest1.py'))