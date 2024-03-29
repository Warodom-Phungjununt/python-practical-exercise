try:
    satisfaction_score = int(11)
except ValueError:
    print("Error: Invalid input. Please enter a valid numeric value for satisfaction score.")
else:
    if 1 <= satisfaction_score <= 10:
        print("Thank you for your feedback!")
    else:
        print("Invalid satisfaction score. Please provide a score between 1 and 10.")
finally:
    print("Customer feedback collection completed.")

# -----------[Output]-----------

# Invalid satisfaction score. Please provide a score between 1 and 10.
# Customer feedback collection completed.