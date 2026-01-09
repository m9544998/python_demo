def inch_to_cm(inch):
    return inch * 2.54

inch = float(input("Enter the length in inches: "))
cm = inch_to_cm(inch)
print(f"The length in centimeters is: {cm}")