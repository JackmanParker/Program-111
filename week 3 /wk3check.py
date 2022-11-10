def miles_per_gallon(startod, endod , gallons):
    return (endod - startod) / gallons

def lp100k_from_mpg(mpg):
    return 235.215 / mpg

def main():
    start = float(input("What is your starting odometer: "))
    end = float(input("What is your ending odometer: "))
    gas = float(input("How many gallons of gas was used (Gallons): "))
    mpg = miles_per_gallon(start, end, gas)
    lp100k = lp100k_from_mpg(mpg)
    print(f"{mpg :.1f} miles per gallon")
    print(f"{lp100k:.2f} liters per 100 kilometers")
main()



