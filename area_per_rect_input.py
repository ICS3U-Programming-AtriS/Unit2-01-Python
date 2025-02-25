#!/usr/bin/env python3
# Created By: Atri Sarker
# Date: Feb 24, 2025
# Calculator for the area and perimeter of a rectangle

# Text Effects
BLUE = "\033[0;34m"
GREEN = "\033[0;32m"
BOLD_W = "\033[1m"  # BOLD WHITE
BOLD_C = "\033[1;36m"  # BOLD CYAN
BOLD_P = "\033[1;35m"  # BOLD PURPLE
WHITE = "\033[0m"  # Default Effect
SUP_2 = "\u00b2"  # Squared Symbol (^2)


def main():
    print(f"{BOLD_W}[#]Enter the Dimensions of the Rectangle:")
    # Get Length of Rectangle
    length = float(input(f"{BLUE}[##]Enter length (cm):{WHITE} "))
    # Get Width of Rectangle
    width = float(input(f"{GREEN}[##]Enter width (cm):{WHITE} "))
    # Calculate the Area of the Rectangle
    area = length * width
    # Calculate the Perimeter of the Rectangle
    perimeter = 2 * (length + width)
    # Display the Area
    print(f"{BOLD_C}[###]The area of the rectangle is {area:0.2f}cm{SUP_2}")
    # Display the Perimeter
    print(f"{BOLD_P}[###]The perimeter of the rectangle is {perimeter:0.2f}cm")


if __name__ == "__main__":
    main()
