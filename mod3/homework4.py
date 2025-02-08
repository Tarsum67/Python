'''
Homework4
Name: "Travis Routhier"
github link:"https://github.com/Tarsum67/Python"
'''

def grade_calculator(score):
    # your code here
    if score < 0 or score > 100:
        return 'Enter a grade between 0-100'
    elif score >= 90:
        return 'A'
    elif score >= 80:
        return 'B'
    elif score >= 70:
        return 'C'
    elif score >= 60:
        return 'D'
    elif score >= 0 and score <= 100:
        return 'F'
    elif score < 0 or score > 100:
        return 'Enter a grade between 0-100'

def even_or_odd(num):
    # your code here
    if num % 2 == 0:
        return 'even'
    else:
        return 'odd'
     



if __name__ == "__main__":
    import doctest
    print(doctest.testfile('doctest4.py'))