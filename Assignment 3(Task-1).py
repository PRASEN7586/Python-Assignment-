
def factorial(n):

  if n < 0:
    return "Factorial is not defined for negative numbers!"
  elif n == 0:
    return 1
  else:
    result = 1
    for i in range(1, n + 1):
      result *= i
    return result

sample = 5
output = factorial(sample)
print(f"The factorial of {sample} is: {output}")
