'''
Homework15
Name: "Travis Routhier"
github link:"https://github.com/Tarsum67/Python" 
'''

def factorial(n):
    # if n = 1 or 0 return 1
    if n == 0 or n == 1:
        return 1
     # Recursive case
    else:
        return n * factorial(n - 1)
  

def main(num1):
     # Call the factorial function
    result = factorial(num1)
    # Print the result
    print(f'"The factorial of {num1} is {result}."')#had to add th '' to pass test
if __name__ == "__main__":
    import doctest
    print(doctest.testfile('doctest15.py'))