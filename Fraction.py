"""
Khanh Vu
U56604117
The program determines if a fraction is Proper Fraction, Improper Fraction or Mixed Fraction
"""
import math

numerator = int(input("Enter a numerator: Value must be greater than 0: "))
while numerator < 0:
    numerator = int(input("Please re-enter the numerator. Value must be greater than 0: "))
denominator = int(input("Enter a denominator: Value must be greater than 0: "))
while denominator < 0:
    denominator = int(input("Please re-enter the denominator. Value must be greater than 0: "))
if numerator < denominator:
    if math.gcd(numerator, denominator) == 1:
        print(f"{numerator}/{denominator} is a proper fraction")
        print(f"This proper fraction cannot be reduced any further")
    elif math.gcd(numerator, denominator) != 1:
        print(f"{numerator}/{denominator} is a proper fraction")
        print("This proper can be reduced to",int(numerator/math.gcd(numerator, denominator)),"/",int(denominator/math.gcd(numerator, denominator)))
elif numerator > denominator:
    if math.gcd(numerator, denominator) == 1:
        print(f"{numerator}/{denominator} is an improper fraction")
        print(f"The mixed number is {int(numerator/math.gcd(numerator, denominator))}/{int(denominator/math.gcd(numerator, denominator))}")
    elif math.gcd(numerator, denominator) != 1:
        print(f"{numerator}/{denominator} is an improper fraction")
        print("This proper can be reduced to", int(numerator/denominator))
        if (numerator/denominator)-(numerator//denominator) == 0:
            print("The whole number is",int(numerator/denominator))
        else:
            print(f"The mixed number is {numerator//denominator} and {int(numerator/math.gcd(numerator, denominator))}/{int(denominator/math.gcd(numerator, denominator))}")
else:
    print("The whole number is 1")
