from math_operations import calculator
from math_operations import geometry

result = calculator.add(5, 3)
print("Addition result:", result)

result = calculator.subtract(10, 4)
print("Subtraction result:", result)


result = geometry.rectangle_area(9, 14)
print("Rectangle Area result:", result)

result = geometry.triangle_area(12, 8)
print("Triangle Area result:", result)

result = geometry.circle_area(3)
result = round(result, 2)
print("Circle Area result:", result)
