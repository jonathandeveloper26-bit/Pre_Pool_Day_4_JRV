### Task 3.3: Vigenere Cipher - Easy

possibleoptions = "abcdefghijklmnopqrstuvwxyz"

### Test "attack", "bald" -> "bteddk"
message, key = input("Enter your Message: "), input("Enter your key Phrase: ")
encrypted_message = ""

for i in range(len(message)):
    key_amount = possibleoptions.index(key[i%len(key)])
    #print(f"key Letter: {key[i%len(key)]}\nkey Amount: {key_amount}")
    encrypted_message += possibleoptions[(possibleoptions.index(message[i]) + key_amount) % len(possibleoptions)]

print(f"Original Message: {message}")
print(f"Encrypted Message: {encrypted_message}")

decrypted_message = ""
for i in range(len(encrypted_message)):
    key_amount = possibleoptions.index(key[i%len(key)])

    decrypted_message += possibleoptions[possibleoptions.index(encrypted_message[i]) - key_amount if possibleoptions.index(encrypted_message[i]) - key_amount >= 0 else len(possibleoptions) + (possibleoptions.index(encrypted_message[i]) - key_amount)]
print(f"Decrypted Message: {decrypted_message}")




### Task 3.3B (allowing for UTF-8)

message, key = input("Enter your Message: ").encode("utf-8"), input("Enter your key Phrase: ").encode("utf-8")
# print(message, key)
# print(f"Message Length: {len(message)}")
# print(f"Key Length: {len(key)}")
encrypted_message = ""

for i in range(len(message)):
    # print(f"Message[{i}]: {message[i]}")
    # print(f"Key[{i}]: {key[i%len(key)]}")
    # print(f"Message + Key: {message[i] + key[i%len(key)]}")
    encrypted_message += chr(message[i] + key[i%len(key)])
    # print(f"Letter {i}: {encrypted_message}")

print(f"Original Message: {message.decode("utf-8")}")
print(f"Encrypted Message: {encrypted_message}")

decrypted_message = ""
print(f"Encrypted Message: {encrypted_message}")
for i in range(len(encrypted_message)):
    #print(f"Encrypted Message[{i}]: {ord(encrypted_message[i])}")
    decrypted_message += chr(ord(encrypted_message[i]) - key[i%len(key)])

print(f"Decrypted Message: {decrypted_message}")

    