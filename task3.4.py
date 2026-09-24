# Allowed letters

## Use Task 3.4_A.py to generate encrypted text using a key of length (any) 
# Use those values in this script.


possibleletters = "abcdefghijklmnopqrstuvwxyz"
encrypted_message, key_length = input("Enter your Encrypted Message: "), int(input("Enter your Key Length: "))

### Begin Decryption Process (only knowing len(key))
# Stores each letter into a list based on the key length (#Lists = Key Length)
stored_lists = [[]]
for i in range(len(encrypted_message)):
    try:
        stored_lists[i%key_length].append(encrypted_message[i])
    except:
        stored_lists.append([encrypted_message[i]])

# Calculate Frequencies of all letters
frequencies = []
for list in stored_lists:
    em_freq = {}
    for item in list:
        if item in possibleletters:
            if item in em_freq:
                em_freq[item] += 100 / len(list)
            else:
                em_freq[item] = 100 / len(list)
        else:
            continue
    frequencies.append(em_freq)


# Calculate Ceaser Cipher Shifts required for each array
ceaser_cipher_shifts = []
for em_freq in frequencies:
    freq = 0
    key_letter = ""
    for key in em_freq:
        if em_freq[key] > freq:
            key_letter = key
            freq = em_freq[key]
        else:
            continue
    ceaser_cipher_shifts.append(4 - possibleletters.index(key_letter)%26)  # 4 because the letter 'e' is the most common

# Decrypt into Un-encrypted Lists
stored_lists_decrypted = [[]]

for i in range(len(stored_lists)):
    for j in range(len(stored_lists[i])):
        shifted_char = possibleletters[(possibleletters.index(stored_lists[i][j])+ceaser_cipher_shifts[i])%26] if stored_lists[i][j] in possibleletters else stored_lists[i][j]
        try: 
            stored_lists_decrypted[i].append(shifted_char)
        except:
            stored_lists_decrypted.append([shifted_char])


# Recombine Message

decrypted_message = ""

for i in range(len(stored_lists_decrypted[0])):
    for list in stored_lists_decrypted:
        try:
            decrypted_message += list[i]
        except:
            continue

print(decrypted_message)
print(ceaser_cipher_shifts)
