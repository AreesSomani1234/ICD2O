# car_type = "helloWorldWorldHello"

# def last_three(car_type):
#     length = len(car_type)
#     l_three = car_type[-9:-2]
#     return l_three

# print(last_three(car_type))




import math

def cosine_law(a, b, c):
    # Calculate angle C using the law of cosines
    numerator = a**2 + b**2 - c**2
    denominator = 2 * a * b
    print(numerator,denominator)
    angle_C_radians = math.acos(numerator / denominator)
    angle_C_degrees = math.degrees(angle_C_radians)
    return angle_C_degrees

def main():
    # Input side lengths
    side_a = float(input("Enter the length of side a: "))
    side_b = float(input("Enter the length of side b: "))
    side_c = float(input("Enter the length of side c: "))

    # Calculate angle C
    angle_C = cosine_law(side_a, side_b, side_c)

    print("Angle C is:", angle_C)

if __name__ == "__main__":
    main()