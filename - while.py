# Lela Parks
# Nov 19, 2024

# Problem 1: Infinite Loop
# Infinite loop that prints "Infinite"
# while True:
#     print("Infinite")

# To stop the loop, use ctrl-C (or command-C on macOS) to break the loop.

# ============================================================================

# Problem 2: List Creation and While Loop
# Initialize list L with two numbers
L = [57, 83]

# Initialize counter
counter = 0

# While loop to append counter values to the list
while counter <= 10:
    L.append(counter)
    counter += 1

# Print how many elements are in the list and what the third element is
print(f"The list has {len(L)} elements.")
print(f"The third element in the list is {L[2]}.")

# ============================================================================

# Problem 3: User Input Until Sum Exceeds 100
# Initialize an empty list to store numbers
numbers = []
total_sum = 0

# While loop that asks for input until the sum exceeds 100
while total_sum <= 100:
    user_input = input("Enter a number: ")
    
    try:
        # Convert input to integer and append to the list
        num = int(user_input)
        numbers.append(num)
        
        # Update the total sum
        total_sum += num
    except ValueError:
        print("Please enter a valid number.")

# After the loop ends, print the list of numbers and the total sum
print(f"The list of numbers entered is: {numbers}")
print(f"The total sum of the numbers is: {total_sum}")


# Notes: 
# Problem one through three are similar to previous modules such as Module 4, 5, and 6 when it comes to creating lists
# and the while function.

# When it comes to placing in algoritms, num, total sum, and repeated usasge of codes like in the current and pervious models
# That we do now.