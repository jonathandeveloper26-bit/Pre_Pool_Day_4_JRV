### Task 1.1
# Evaluate and explain the following lines: (Done in Terminal)
# ✓ (42 >12): True (Boolean Operator 42 is greater than 12)
# ✓ (12 =12): Sytax Error (12 cannot be a variable to be assigned a value)
# ✓ (12 ==12): True (12 is equivalent to 12 )
# ✓ (”hello” == ”world”): False ("Hello" is not equal to "World")
# ✓ (218 >=118): True (Boolean Operator 218 is greater than or equal to 118)
# ✓ (”a”.upper() == ”A”): True (upper applies to "a" prior to checking if equal to "A")
# ✓ (1 ∗2∗3∗4<=9): False (math operations done prior to checking - > 24 <= 9 is False)
# ✓ (”z”in ”azerty”): True ("z" exists in "azerty")


### Task 1.2 (Request Integer and Check if Equal to 42 - Print "That is Correct" if true)

user_int = int(input("Enter an Integer: "))
if (user_int == 42):
    print("That is correct!")
else: 
    print("That is not correct!")

### Task 1.3 (Check if user input is even or odd)

user_int = int(input("Enter an Integer: "))
if(user_int % 2 == 0):
    print("This integer is even")
elif (user_int %2 == 1):
    print("This integer is odd")

### Task 1.4 (Prompt user for string)
user_password = input("Please enter your password: ")
if user_password == "open sesame":
    print ("access granted")
elif user_password == "will you open, you goddamn !@&/°":
    print ("access fucking granted")
else:
    print("permission denied")

### Task 1.5 (Multiple conditions, printing only those that are true, including option for all false)
user_int = int(input("Enter an integer: "))
output = ""
anytrue = False

if user_int == 42:
    anytrue = True
    output += "a"
if user_int <= 21:
    anytrue = True
    output += "b"
if user_int % 2 == 0:
    anytrue = True
    output += "c"
if user_int / 2 < 21:
    anytrue = True
    output += "d"
if user_int % 2 == 1 and user_int >= 45:
    anytrue = True
    output += "e"

if not anytrue:
    output += "f"

print(output)

### Task 1.6

## Original Code given in Task
# a == 42
# b == 41
# if a = b
# print("A and B is the sames")
# if b =< a
# print("B is equal or lower as A")
# if b =! a
# print("B his different from A")


## Fixed Code
a = 42
b = 41
if a == b:
    print("A and B are the equal.")
if b <= a:
    print("B is equal to or lower than A.")
if b != a:
    print("B is not equal to A.")