'''
Homework2
Name: "Travis Routhier"
github link:"https://github.com/Tarsum67/Python"
'''

def inches_to_cm(inches):
    # your code here
    conversion = 2.54
    sum = inches * conversion
    return sum

def feet_to_meters(feet):
    # your code here
    conversion = .3048
    sum = feet * conversion
    return  round(sum,2)

def lbs_to_kg(lbs):
    # your code here
    conversion = .4536
    sum = lbs * conversion
    return round(sum,2)

def hours_to_minutes(hrs):
    # your code here
    conversion = 60
    sum = hrs * conversion
    return sum

 

if __name__ == "__main__":
    import doctest
    print(doctest.testfile('doctest2.py'))
    
    