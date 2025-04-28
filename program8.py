import math

def distance_between_points(x1, y1, x2, y2):
    """
    Calculate the distance between two points (x1, y1) and (x2, y2).
    """
    distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    return distance

# Example usage
if __name__ == "__main__":
    x1, y1 = map(float, input("Enter coordinates of the first point (x1, y1): ").split())
    x2, y2 = map(float, input("Enter coordinates of the second point (x2, y2): ").split())
    
    result = distance_between_points(x1, y1, x2, y2)
    print(f"The distance between the points is: {result}")