num1= int(input("enter first number: "))
num2= int(input("enter second number: 8"))

print("the sum of these is: ",num1+num2)

side= float(input("enter the side of the square: "))
print("The area of the square is: ", side * side)

def rectangle_area_perimeter(length, breadth):
    area = length * breadth
    perimeter = 2 * (length + breadth)
    return area, perimeter

# Example usage
length = 5
breadth = 3
area, perimeter = rectangle_area_perimeter(length, breadth)
print(f"Area of Rectangle: {area}")
print(f"Perimeter of Rectangle: {perimeter}")

