#!/usr/bin/env python3

# Created by: Patrick Gemmell
# Created on: September 12 2019
# This calculates the price of a user inputed pizza

import constants


def main():
    # this function calculates the cost of pizza

    diameter = int(input("Enter the diameter of the circle (inch): "))

    sub_total = constants.LABOR + constants.RENT + \
        (diameter * constants.COST_PER_INCH)
    total = sub_total + (sub_total * constants.HST)

    print("")
    print("The cost for a {0} inch pizza is: ${1:,.2f}"
          .format(diameter, total))


if __name__ == "__main__":
    main()
