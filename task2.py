### Task2.1
# Print all integers from 1 to 1000
for i in range(1,1001):
    print(i)

### Task 2.2
# Prompt user for string, display each letter twice
user_string = input("Enter a word: ")
output_string = ""
for char in user_string:
    output_string += char *2
print(output_string)

### Task 2.3
# Print all integers, in decreasing order from 10 000 to 1, that are divisible by 7
for i in range(10001,1,-1):
    if i % 7 == 0:
        print(i)

### Task 2.4
# For all integers from-30 to 30:
# ✓ if it's a multiple of 3, display ”Fizz”;
# ✓ if it's a multiple of 5, display ”Buzz”;
# ✓ if it's a multiple of 3 and 5, display ”FizzBuzz”;
# ✓ if it does not meet any of the previous conditions, just print the integer itself

for i in range(-30,30):
    condition_met = False
    output = ""
    if i % 3 == 0:
        output+="Fizz"
        condition_met = True
    if i%5 == 0:
        output+="Buzz"
        condition_met = True
    if not condition_met:
        output += str(i)
    print(output)


    
