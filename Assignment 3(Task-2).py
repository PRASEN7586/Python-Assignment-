
import math

def perform_math_calculations():
 
  try:
    num_str = input("Enter a number: ")
    number = float(num_str)

   
    if number >= 0:
      sqrt_result = math.sqrt(number)
      print(f"Square root of {number}: {sqrt_result}")
    else:
      print(f"Square root is not defined for negative numbers.")

    
    if number > 0:
      log_result = math.log(number)
      print(f"Natural logarithm (base e) of {number}: {log_result}")
    else:
      print(f"Natural logarithm is not defined for non-positive numbers.")

    
    sine_result = math.sin(number)
    print(f"Sine of {number} (in radians): {sine_result}")

  except ValueError:
    print("Invalid input. Please enter a valid number.")


perform_math_calculations()