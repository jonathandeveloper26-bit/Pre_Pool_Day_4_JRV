### Task 3.2: Ceaser Cipher Shift - Any Message (UTF-8)

message, shift = input("Enter your message: ").encode("utf-8"), int(input("Enter your shift: "))

encrypted_message = ""
for char in message: 
    encrypted_message += chr(char + shift)

print(f"Original Message: {message.decode("utf-8")}")
print(f"Encrypted Message: {encrypted_message}")