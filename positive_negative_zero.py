#!/usr/bin/env python3

# Created by: Liam Hearty
# Created on: September 2019
# This program tells user if their number is positive, negative, or zero.


def main():
    # if ... then ... elseif ... else example

    # input
    chosen_number = int(input("Enter a whole number (negative or positive): "))

    if chosen_number <= -1:
        print("(-) negative")
    elif chosen_number >= 1:
        print("(+) positive")
    else:
        print("(0) neither, you thought you were tricky huh.")

if __name__ == "__main__":
    main()
