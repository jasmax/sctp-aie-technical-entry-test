# Question 3 - String Manipulation
# Topic: Name Formatting Utility
#
# Task 1:
# Write a function called formatName(firstName, lastName) that accepts two strings
# and returns a formatted string in this format: "lastName, firstName"
# Example: formatName("John", "Smith") → "Smith, John"

def formatName(firstName, lastName):
    # Add your code here
    return f"{lastName.capitalize()}, {firstName.capitalize()}"


# Task 2:
# Write a function called formatInitials(firstName, lastName) that returns the
# initials of the person as a string in uppercase.
# Example: formatInitials("john", "smith") → "J.S."
# Note: your function should handle inputs in any case (upper, lower, or mixed)
# and always produce properly capitalised output.

def formatInitials(firstName, lastName):
    # Add your code here
    return f"{firstName[0].upper()}.{lastName[0].upper()}."


# Task 3:
# Call both functions with the following inputs and print each result:
#   formatName("Alice", "Tan")  → Expected: "Tan, Alice"
#   formatName("bob", "lim")    → Expected: "Lim, Bob"
#   formatInitials("Alice","Tan") → Expected: "A.T."
#   formatInitials("bob","lim")   → Expected: "B.L."

# Add your code here
print(formatName("Alice", "Tan"))       # Expected: Tan, Alice
print(formatName("bob", "lim"))         # Expected: Lim, Bob
print(formatInitials("Alice", "Tan"))   # Expected: A.T.
print(formatInitials("bob", "lim"))     # Expected: B.L.

"""
def run_tests():
    passed = 0
    failed = 0

    def check(label, initial, result, expected):
        nonlocal passed, failed
        status = "PASS" if result == expected else "FAIL"
        print(f"  Initial  : {initial}")
        print(f"  Result   : {result}")
        print(f"  Expected : {expected}")
        print(f"  [{status}] {label}")
        print()
        if status == "PASS":
            passed += 1
        else:
            failed += 1

    # --- formatName tests ---
    check("formatName standard case",
          ("Alice", "Tan"), formatName("Alice", "Tan"), "Tan, Alice")

    check("formatName lowercase input",
          ("bob", "lim"), formatName("bob", "lim"), "Lim, Bob")

    # --- formatInitials tests ---
    check("formatInitials standard case",
          ("Alice", "Tan"), formatInitials("Alice", "Tan"), "A.T.")

    check("formatInitials lowercase input",
          ("bob", "lim"), formatInitials("bob", "lim"), "B.L.")

    print(f"{passed}/{passed + failed} tests passed.")


run_tests()
"""