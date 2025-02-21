'''
Homework16
Name: "Travis Routhier"
github link:"https://github.com/Tarsum67/Python" 
'''

def pythagorean_thm(tuple):
    # your code here
    a=tuple[0]
    b=tuple[1]
    result = (a**2 + b**2)**.5
    return int(result) if result.is_integer() else round(result, 2)

def distance_between_points(tuple1,tuple2):
    x1=tuple1[0]
    y1=tuple1[1]
    x2=tuple2[0]
    y2=tuple2[1]
    result = ((x2 - x1)**2 + (y2 - y1)**2)**.5
    return int(result) if result.is_integer() else round(result, 2)

if __name__ == "__main__":
    import doctest
    print(doctest.testfile('doctest16.py'))