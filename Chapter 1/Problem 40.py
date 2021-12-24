#Exercise 40

def normBMI(weight, height):
    return weight/height**2


def convertedBMI(weight, height):
    weight *= 0.4535919737
    height *= 0.0254
    return normBMI(weight,height)


weight = float(input("Please enter your wight in kilograms: "))
height = float(input("Plase enter your height in meters: "))

print(normBMI(weight,height))



weight_in_pounds = float(input("Please enter your weight in pounds: "))
height_in_inches = float(input("Plase enter your height in inches: "))

print(convertedBMI(weight_in_pounds,height_in_inches))

