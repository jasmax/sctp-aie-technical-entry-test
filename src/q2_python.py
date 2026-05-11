# Question 2 - Arrays and Loops
# Topic: Inventory Tracker
#
# Task 1:
# Declare an empty list called inventory to store item names as strings.

# Add your code here
inventoryList = []
# align naming with requirement
inventory = inventoryList

# Task 2:
# Write a function called addItem(itemName) that adds the given item to the
# inventory list. If the item already exists, print a message instead of adding it.
# Example message: "Mouse is already in inventory."

def addItem(itemName):
    # Add your code here
    if itemName in inventoryList:
        print(f"{itemName} is already in inventory.")
    else:
        inventoryList.append(itemName)

# Task 3:
# Write a function called listInventory() that prints all items in the inventory.
# If the inventory is empty, print: "Inventory is empty."

def listInventory():
    # Add your code here
    if len(inventoryList) == 0:
        print("Inventory is empty.")
    else:
        print(f"Inventory: {inventoryList}")

# Task 4:
# Call the functions in this order and observe the output:
addItem("Laptop")
addItem("Mouse")
addItem("Keyboard")
addItem("Mouse")   # Should trigger duplicate warning
listInventory()

# Expected output:
# Mouse is already in inventory.
# Inventory: ['Laptop', 'Mouse', 'Keyboard']
"""
def run_tests():
    global inventory
    import io, sys

    passed = 0
    failed = 0

    def check(label, initial, result, expected):
        nonlocal passed, failed
        status = "PASS" if result == expected else "FAIL"
        print(f"  Initial  : {initial}")
        print(f"  Result   : {result}")
        print(f"  Expected : {expected}")
        print(f"  [{status}] {label}\n")
        passed += status == "PASS"
        failed += status == "FAIL"

    def get_output(fn, *args):
        buf = io.StringIO()
        sys.stdout = buf
        fn(*args)
        sys.stdout = sys.__stdout__
        return buf.getvalue().strip()

    # Test 2: Final inventory list
    check("Final inventory list",
          [],
          inventory,
          ["Laptop", "Mouse", "Keyboard"])
    
    # Test 1: Duplicate warning message
    check("Duplicate warning message",
          inventory.copy(),
          get_output(addItem, "Mouse"),
          "Mouse is already in inventory.")

    print(f"{passed}/{passed + failed} tests passed.")

run_tests()
"""