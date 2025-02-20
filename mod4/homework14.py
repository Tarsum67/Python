'''
Homework14
Name: "Travis Routhier"
github link:"https://github.com/Tarsum67/Python" 
'''
#your global variables go here.


def convert_to_kg(lbs):
    #your code here
    kg = lbs * 0.453592
    return round(kg,2)

def convert_to_meters(inches):
    meters = round(inches * 0.0254, 2)
    return meters

def bmi_calculation(lbs,height):
    # your code here
    mResult = convert_to_meters(height)
    kResult = convert_to_kg(lbs)
    bmi = round(kResult / (mResult ** 2), 1)
    if(bmi < 18.5):
        return "underweight"
    elif(bmi >= 18.5 and bmi < 24.9):
        return "normal weight"
    elif(bmi >= 25 and bmi < 29.9):
        return "overweight"
    elif(bmi >= 30):
        return "obese"

if __name__ == "__main__":
    import doctest
    print(doctest.testfile('doctest14.py'))