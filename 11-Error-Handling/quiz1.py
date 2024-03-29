try:
    num1 = float(5.5)
    num2 = float(0)
    result = num1 / num2
    print("Quotient:", result)
except ZeroDivisionError:
    print("Error: Cannot divide by zero.")
except ValueError:
    print("Error: Please enter valid numeric values.")

# -----------[Output]-----------

# Error: Cannot divide by zero.