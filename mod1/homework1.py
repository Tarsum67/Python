'''
Homework1
Name: "Travis Routhier"
github link:"https://github.com/Tarsum67/Python" 
'''

import random

def check(guess, actual_number):
    difference = abs(guess - actual_number)

    if difference == 0:
        return 'You Got It!'
    elif difference <= 4:
        return 'Very Hot'
    elif difference <= 14:
        return 'Hot'
    elif difference <= 24:
        return 'Cool'
    elif difference >= 25:
        return 'Cold'
   
    
def main(actual_number):
    
    for i in range(0, 100):
        guess = random.randint(1, 100)
        print(check(guess, actual_number))
        if check(guess, actual_number) == 'You Got It!':
            break
        

if __name__ == "__main__":
    import doctest
    print(doctest.testfile('doctest1.py'))