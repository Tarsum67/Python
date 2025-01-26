'''
Homework2
Name:"Travis Routhier"
github link:"https://github.com/Tarsum67/Python" 
'''

def birthday(month,day,year):
    # your code here
    return print(f"'Your birthday is {month} {day}, {year}.'")

def address(street,city,state,zipcode):
    #your code here
    return print(f"'Your address is {street}, {city}, {state}, {zipcode}.'")

if __name__ == "__main__":
    import doctest
    print(doctest.testfile('doctest25.py'))