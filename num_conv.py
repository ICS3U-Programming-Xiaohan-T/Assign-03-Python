#!/usr/bin/env python3
# Created By: Xiaohan
# Date: Apr 5, 2025
# This program compares 3 numbers from smallest to biggest


def main():
    # Display welcoming message
    print("Hello! Welcome to the program!")
    # Get user input of the first number as a string
    first_number_string = input("Please enter the fist number as an integer: ")
    # Get user input of the second number as a string
    second_number_string = input("Please enter the Second number as an integer: ")
    # Get user input of the third number as a string
    third_number_string = input("Please enter the third number as integer: ")
    # try catch statement
    try:
        # Casting number 1 into integer
        first_number = int(first_number_string)
        # Casting number 2 into integer
        second_number = int(second_number_string)
        # Casting number 3 into integer
        third_number = int(third_number_string)

        # Check if all numbers are equal
        numbers_are_equal = False

        # Check if any numbers are equal
        if first_number == second_number == third_number:
            print("All numbers are equal.")
        # Some numbers are equal
        elif (
            first_number == second_number
            or first_number == third_number
            or second_number == third_number
        ):
            print("Some numbers are equal.")

        # where numbers are not equal
        if not numbers_are_equal:
            # Comparing number 1 with number 2 and 3
            if first_number < second_number and first_number < third_number:
                # If above is true, comparing number 2 and 3
                if second_number < third_number:
                    # Display the result from smallest to largest
                    print(
                        "The number order is: {} < {} < {}".format(
                            first_number, second_number, third_number
                        )
                    )
                else:
                    # Display the result from smallest to largest
                    print(
                        "The num order is: {} < {} < {}".format(
                            first_number, third_number, second_number
                        )
                    )
            else:
                # compare number 2 with number 1 and 3
                if second_number < first_number and second_number < third_number:
                    # Compare number 1 with number 3
                    if first_number < third_number:
                        # Display the result from smallest to largest
                        print(
                            "The num order is: {} < {} < {}".format(
                                second_number, first_number, third_number
                            )
                        )
                    else:
                        # Display the result from smallest to largest
                        print(
                            "The num order is: {} < {} < {}".format(
                                second_number, third_number, first_number
                            )
                        )
                else:
                    # Compare number 1 with number 2
                    if first_number < second_number:
                        # Display the result from smallest to largest
                        print(
                            "The number order is: {} < {} < {}".format(
                                third_number, first_number, second_number
                            )
                        )
                    else:
                        # Display the result from smallest to largest
                        print(
                            "The number is: {} < {} < {}".format(
                                third_number, second_number, first_number
                            )
                        )
        # Show the smallest and largest number
        smallest = min(first_number, second_number, third_number)
        largest = max(first_number, second_number, third_number)

        # Display the smallest and largest number
        print("The smallest number is: {}".format(smallest))
        print("The largest number: {}".format(largest))

        # Calculate and show the average and save it for 2 decimal places
        average = (first_number + second_number + third_number) / 3
        print("The average of the numbers is: {:.2f}".format(average))

    except Exception:
        # Exceptions where users did not input a number as integer
        print("Invalid input, please try again.")

    # Ending message
    print("Thank you for using the program!")


if __name__ == "__main__":
    main()
