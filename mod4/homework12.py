'''
Homework12
Name: "Travis Routhier"
github link:"https://github.com/Tarsum67/Python" 
'''
def rectangle(side1,side2):
    side1 * side2
    return print(f"'The area of the rectangle is {side1 * side2} square units'")
    
   
def circle(radius):
    area = radius * radius * 3.14
    return print(f"'The area of a circle is {area} square units'")
   


if __name__ == "__main__":
    import doctest
    print(doctest.testfile('doctest12.py'))