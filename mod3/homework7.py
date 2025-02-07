'''
Homework7
Name: "Travis Routhier"
github link:"https://github.com/Tarsum67/Python"
'''

def fizzbuzz(n):
    for num in range(1, n + 1):  
        if num % 3 == 0 and num % 5 == 0:
            print("FizzBuzz")
        elif num % 3 == 0:
            print("Fizz")
        elif num % 5 == 0:
            print("Buzz")
        else:
            print(num)

def scholarship_eligibility(gpa,credits):
    # your code here
    if gpa >= 3.7 and credits >= 60:
        return True
    else:
        return False
    

def max_of_three_numbers(num1,num2,num3):
    # your code here
    if num1 > num2 and num1 > num3:
        return num1
    elif num2 > num1 and num2 > num3:
        return num2
    else:
        return num3


if __name__ == "__main__":
    import doctest
    print(doctest.testfile('doctest7.py'))