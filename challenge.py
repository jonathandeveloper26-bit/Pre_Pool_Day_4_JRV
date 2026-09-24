### CHALLENGE
# Write the shortest code possible that does the following:
# ✓ prompt the user simultaneously for an integer and a string;
# ✓ if the integer is 0, then quit;
# ✓ if the string contains a vowel, display the integer;
# ✓ if the integer is greater than or equal to 42, display the integer;
# ✓ else display the string

a,b = int(input("Input an integer: ")), input("Input a string: ")
quit() if a == 0 else print(*[a] if any(vowel in b for vowel in "aeiou") else [], a if a >= 42 else b)

