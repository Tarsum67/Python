'''
Homework3
Name: "Travis Routhier"
github link:"https://github.com/Tarsum67/Python"
'''

def positive_or_negative(num):
    # your code here
    if num > 0:
        return True
    else:
        return False

def is_able_to_drive(num):
    # your code here
    if num >= 16:
        return True
    else:
        return False

def is_able_to_vote(num):
    # your code here
    if num >= 18:
        return True
    else:
        return False

def can_buy_alcohol(num):
    # your code here    
    if num >= 21:
        return True
    else:
        return False

def senior_discount(num):
    # your code here
    if num >= 65:
        return True
    else:
        return False
   

if __name__ == "__main__":
    import doctest
    print(doctest.testfile('doctest3.py'))