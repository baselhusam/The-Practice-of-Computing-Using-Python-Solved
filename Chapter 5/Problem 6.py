#Exercise 6

def energy(mass):
    return "Energy = {} meter-Kilogram-second system".format(mass**2)

mass = float(input("Enter the mass: "))

print(energy(mass))