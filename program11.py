import math

def area_of_circle(radius):
    """Calculate the area of a circle given its radius."""
    if radius < 0:
        raise ValueError("Radius cannot be negative")
    return math.pi * radius ** 2

# Example usage
if __name__ == "__main__":
    try:
        radius = float(input("Enter the radius of the circle: "))
        area = area_of_circle(radius)
        print(f"The area of the circle with radius {radius} is {area:.2f}")
    except ValueError as e:
        print(e)