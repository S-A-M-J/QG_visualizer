#QG_calc.py

import math

from colorama import Fore, Style



def calculate_sphere_data(radius, density):
    volume = 4/3 * math.pi * radius **3
    mass = volume * density
    return mass

def calculate_gravity_acceleration(mass, distance):
    gravity = mass * (6.67408 * 10**-11) / distance **2
    return gravity

def main():

    print(math.__file__)

    radius = float(input("Enter the radius of the sphere in meters: "))
    distance = float(input("Enter the distance of the sphere middle to the QG: "))
    density_1 = float(input("Enter the density of the first sphere material in g/ccm^3: "))
    density_2 = float(input("Enter the density of the second sphere material in g/ccm^3: "))
    mass_1 = calculate_sphere_data(radius, density_1*1000)
    mass_2 = calculate_sphere_data(radius, density_2*1000)
    gravity_1 = calculate_gravity_acceleration(mass_1, distance)
    gravity_2 = calculate_gravity_acceleration(mass_2, distance)
    print("The mass of the first sphere is {:.2f} kg ".format(mass_1) + "and it's gravity is {:e}".format(gravity_1) + " m/s^2")
    print("The mass of the second sphere is {:.2f} kg ".format(mass_2) + "and it's gravity is {:e}".format(gravity_2)+ " m/s^2")
    gravity_difference = gravity_1 - gravity_2
    print("The difference in acceleration due to gravity is {:e}".format(abs(gravity_difference))+ " m/s^2")
    if abs(gravity_difference) >= 10**-8:
        print(f"{Fore.GREEN}The difference should be detectable.{Style.RESET_ALL}")
    else:
        print(f"{Fore.RED}The difference is probably not detectable.{Style.RESET_ALL}")

if __name__ == '__main__':
    main()