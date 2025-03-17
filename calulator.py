# calculator.py
def add(x, y):
    """Adds two numbers."""
    return x + y

def subtract(x, y):
    """Subtracts two numbers."""
    return x - y

def multiply(x, y):
    """Multiplies two numbers."""
    return x * y

def divide(x, y):
    """Divides two numbers.  Raises ValueError if dividing by zero."""
    if y == 0:
        raise ValueError("Cannot divide by zero")
    return x / y

def power(x, y):
  """Calculates x raised to the power of y."""
  return x ** y
