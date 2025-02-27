import math

def paint_calc(Height, Width, Coverage):
    area_coverage = math.ceil(Height * Width / Coverage)
    print(f"You will need {area_coverage} cans.")


test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5
paint_calc(Height=test_h, Width=test_w, Coverage=coverage)

def prime_checker(number):
    is_prime = True
    for i in range (2, number):
        if number % i == 0:
            is_prime = False
    if is_prime:
        print("Its a prime")
    else:
        print("Not Prime")


n = int(input("Check this number: "))
prime_checker(number=n)