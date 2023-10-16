# mean_calculator.py

import argparse

def main():
    parser = argparse.ArgumentParser(description="Calculate the mean of a sequence of numbers.")

    # Add the main argument to accept numbers
    parser.add_argument("numbers", metavar="N", type=str, nargs="*", help="A sequence of numbers")

    # Add the base options
    group = parser.add_mutually_exclusive_group()
    group.add_argument("-b", "--binary", action="store_true", help="Interpret numbers as binary")
    group.add_argument("-o", "--octal", action="store_true", help="Interpret numbers as octal")
    group.add_argument("-x", "--hexadecimal", action="store_true", help="Interpret numbers as hexadecimal")

    args = parser.parse_args()

    # Convert the numbers based on the given base
    if args.binary:
        base = 2
    elif args.octal:
        base = 8
    elif args.hexadecimal:
        base = 16
    else:
        base = 10

    try:
        if base != 10:
            numbers = [int(num, base) for num in args.numbers]
        else:
            numbers = [float(number) for number in args.numbers]

        # Calculate the mean
        mean = sum(numbers) / len(numbers)
    except ZeroDivisionError:
        print("Error: No numbers provided.")
        return
    except ValueError:
        print("Error: Invalid number format for the specified base.")
        return

    print(f"Mean: {mean}")

if __name__ == "__main__":
    main()
