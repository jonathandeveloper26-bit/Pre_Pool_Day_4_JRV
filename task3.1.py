### Task 3.1: Ceaser Cipher Shift - Easy

possibleoptions = "abcdefghijklmnopqrstuvwxyz"

message, shift = input("Enter your message: "), int(input("Enter your shift: "))

encrypted_message = ""
for char in message: 
    if char == " ": 
        encrypted_message += " "
    else:
        current_pos = possibleoptions.index(char)
        shifted_pos = (current_pos + shift) % 26
        encrypted_message += possibleoptions[shifted_pos]

print(f"Original Message: {message}")
print(f"Encrypted Message: {encrypted_message}")