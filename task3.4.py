# Allowed letters
possibleletters = "abcdefghijklmnopqrstuvwxyz"

# Generated messsage to use.
original_message = "Python has become one of the most widely used programming languages in the world, and its popularity is no accident. Designed by Guido van Rossum and first released in 1991, the language was built around a philosophy that values readability, simplicity, and clarity. These principles are captured in a short collection of aphorisms known as the Zen of Python, which encourages developers to prefer explicit code over implicit code, simple solutions over complex ones, and readable designs over clever tricks. For professionals working in software development, data analysis, automation, or scientific computing, understanding these principles is the first step toward writing Python that is both effective and maintainable. One of the defining characteristics of Python is its use of indentation to define code blocks. Where many languages rely on braces or keywords to mark the beginning and end of a function or loop, Python uses whitespace. This design choice forces developers to write code with a consistent visual structure, which makes programs easier to read and review. The official style guide, known as PEP 8, recommends using four spaces per indentation level, limiting lines to a reasonable length, and following consistent naming conventions. Functions and variables are typically written in lowercase with underscores, while classes use capitalized words. Adhering to these conventions allows teams to collaborate more smoothly, since everyone can read and understand code written by their colleagues without adjusting to individual habits. Python is a dynamically typed language, meaning that variables do not need to be declared with a specific type before they are used. A variable can hold an integer at one moment and a string the next. This flexibility makes the language approachable and speeds up early development, but it can also introduce errors that only appear at runtime. To address this, modern Python supports optional type hints. By annotating function parameters and return values, developers can document their intentions and use static analysis tools such as mypy to detect mistakes before the code is executed. In larger projects, type hints have become an essential practice, improving reliability and making code easier for new team members to understand. The standard library is another of Python's great strengths. Often described as batteries included, the language ships with modules for working with files, dates, regular expressions, network protocols, data compression, and much more. Before reaching for an external package, experienced developers check whether the standard library already provides what they need. Modules such as collections, itertools, and functools offer powerful tools for handling data efficiently, while pathlib provides a clean, object-oriented approach to working with file system paths. Familiarity with these modules allows developers to write concise solutions without adding unnecessary dependencies to a project. When the standard library is not enough, the Python Package Index offers hundreds of thousands of third-party packages. Libraries such as NumPy and pandas have made Python the leading language for data analysis, while frameworks such as Django and Flask power many web applications. Machine learning tools, including scikit-learn and PyTorch, have further expanded the language's reach. Managing these dependencies properly is an important professional skill. Virtual environments allow each project to maintain its own isolated set of packages, preventing conflicts between projects that require different versions of the same library. Tools such as pip, venv, and more recent options like Poetry and uv help developers create reproducible environments that behave the same way on every machine. Writing clean functions is central to good Python practice. A well-designed function performs a single, clearly defined task, has a descriptive name, and accepts a manageable number of parameters. Docstrings, which are string literals placed at the beginning of a function, class, or module, explain what the code does and how it should be used. Many documentation tools can extract these docstrings automatically, producing reference material with little additional effort. Keeping functions small and focused also makes them easier to test, reuse, and modify as requirements change. Error handling in Python follows the principle that it is often easier to ask for forgiveness than permission. Rather than checking every possible condition in advance, Python code frequently attempts an operation and handles any exceptions that arise. The try and except statements allow developers to respond gracefully to problems such as missing files, invalid input, or network failures. However, good practice requires catching specific exceptions rather than silencing all errors indiscriminately. Broad exception handling can hide genuine bugs and make problems much harder to diagnose. Context managers, used with the with statement, provide a reliable way to manage resources such as files and database connections, ensuring they are properly closed even when an error occurs. Testing is an essential part of professional Python development. The built-in unittest module provides a framework for writing and running tests, while the popular pytest library offers a simpler syntax and a rich ecosystem of plugins. Automated tests verify that code behaves as expected and protect against regressions when changes are made. Many teams integrate their test suites into continuous integration pipelines, so that every proposed change is automatically checked before it is merged. Combined with linters and formatters such as Ruff and Black, testing helps maintain a consistent level of quality across an entire codebase. Performance is sometimes cited as a weakness of Python, since it is generally slower than compiled languages such as C or Rust. In practice, however, this limitation is often less significant than it appears. Many performance-critical libraries are written in compiled languages and exposed through Python interfaces, giving developers speed without sacrificing convenience. When optimization is necessary, profiling tools help identify the specific sections of code that consume the most time. Techniques such as using appropriate data structures, avoiding unnecessary loops, and leveraging vectorized operations can produce substantial improvements. Ultimately, writing professional Python is about more than knowing the syntax. It involves following established conventions, choosing appropriate tools, writing tests, documenting code clearly, and thinking carefully about the people who will read and maintain the work in the future. Python rewards developers who value clarity and discipline, and its supportive global community continues to produce resources, libraries, and guidance that help programmers at every level improve their craft."
original_message = original_message.lower()

# Key for Encryption (used for encrypting and then decrypting and comparing to my analysis)
key = "helloworld"
key_length = len(key)

# Create and Store Encrypted Message
encrypted_message = ""
for i in range(len(original_message)):
    if not original_message[i] in possibleletters:
        encrypted_message += original_message[i]
    else:
        encrypted_message += possibleletters[(possibleletters.index(original_message[i]) + possibleletters.index(key[i%key_length]))%len(possibleletters)]

# Create and Store Decrypted Message (using Key - for comparison)
decrypted_message = ""

for i in range(len(encrypted_message)):
    if encrypted_message[i] in possibleletters:
        decrypted_message += possibleletters[(possibleletters.index(encrypted_message[i]) - possibleletters.index(key[i%key_length]))%len(possibleletters)]
    else:
        decrypted_message += encrypted_message[i]

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
