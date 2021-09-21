#!/usr/bin/env python3

# Created by: Rohnin Barrette
# Created on: Sep 2021
# This function tells the user if the inputted integer is a positive, negative or neutral integer


def main():
    # This function tells the user if the inputted integer is a positive, negative or neutral integer

    # input
    integer = int(input("Enter an Integer here: "))
    print("")

    if integer > 0:
        print("{0} That is a positive integer.".format(integer))
    elif integer < 0:
        print("{0} That is a negative integer.".format(integer))
    else:
        print("{0} That's a zero.".format(integer))

    print("\nDone.")


if __name__ == "__main__":
    main()
