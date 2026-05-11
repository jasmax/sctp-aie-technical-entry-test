# Question 1 - Functions and Conditionals
# Topic: Temperature Converter
#
# Task 1:
# Write a function called convertTemp that accepts two arguments:
#   - value: a numeric temperature value
#   - unit: a string, either "C" for Celsius or "F" for Fahrenheit
#
# The function should:
#   - Convert Celsius to Fahrenheit if unit is "C"  →  Formula: (value × 9/5) + 32
#   - Convert Fahrenheit to Celsius if unit is "F"  →  Formula: (value − 32) × 5/9
#   - Return -1 if unit is neither "C" nor "F"
#   - Round the result to 2 decimal places before returning

def convertTemp(value, unit):
    # Add your code here
    # Convert Celsius to Fahrenheit if unit is "C"
    if unit == "C":
        # Formula: (value × 9/5) + 32, 
        # Round the result to 2 decimal places before returning
        return round((value * 9/5) + 32, 2)
    # Convert Fahrenheit to Celsius if unit is "F"
    elif unit == "F":
        # Formula: (value − 32) × 5/9
        # Round the result to 2 decimal places before returning
        return round((value - 32) * 5/9, 2)
    else:
        # Return -1 if unit is neither "C" nor "F"
        return -1

# Task 2:
# Call the function with the following inputs and print each result:
#   convertTemp(100, "C")     → Expected: 212.0
#   convertTemp(32, "F")      → Expected: 0.0
#   convertTemp(37, "C")      → Expected: 98.6
#   convertTemp("invalid","X")→ Expected: -1

# Add your code here
print(convertTemp(100, "C"))
print(convertTemp(32, "F"))
print(convertTemp(37, "C"))
print(convertTemp("invalid", "X"))

"""
def run_tests():
    # test input and expected result
    tests = [
        (100, "C", 212.0),
        (32,  "F", 0.0),
        (37,  "C", 98.6),
        ("invalid", "X", -1),
    ]

    # result total
    passed = 0
    failed = 0

    for value, unit, expected in tests:
        # call convertTemp function
        result = convertTemp(value, unit)
        # outpust vs expected result
        status = "PASS" if result == expected else "FAIL"
        # print output and test result
        print(f"convertTemp({value!r}, {unit!r}) → output {result}, expected {expected} [{status}]")
        if status == "PASS":
            passed += 1
        else:
            failed += 1
    #print result count
    print(f"\n{passed}/{passed + failed} tests passed.")

run_tests()
"""