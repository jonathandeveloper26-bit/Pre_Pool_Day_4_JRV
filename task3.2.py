### Task 3.2: Ceaser Cipher key - Any Message (UTF-8)

message, key = input("Enter your message: ").encode("utf-8"), int(input("Enter your key: "))

encrypted_message = ""
for char in message: 
    encrypted_message += chr(char + key)

print(f"Original Message: {message.decode("utf-8")}")
print(f"Encrypted Message: {encrypted_message}")

### Decryption: Assume Key Given (utilizing the above code/responses)

encrypted_message = encrypted_message.encode('utf-8')
decrypted_message = ""
for char in encrypted_message: 
    decrypted_message += chr(char - key)

print(f"Decrypted Message: {decrypted_message}")



