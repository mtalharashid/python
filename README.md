# Python Learning Project

This repository contains a collection of Python exercises and practice files that I created while learning Python. The purpose of this project is to practice basic Python concepts, experiment with different libraries, and improve 
my coding skills.

## Project Structure

The project contains multiple Python files and folders. Each Python file focuses on a specific concept or set of exercises. Some folders contain additional resources or organized code snippets, which I will explain in detail later.

Example structure:
```
PYTHON/
│
├── numpy/ # Practice with NumPy library
├── oop/ # Object-Oriented Programming exercises
├── Pandas/ # Pandas library exercises
├── regularExpression/ # Regular expressions practice
├── UnitTesting/ # Unit testing exercises
├── 001.py # Basic Python exercises
├── apis.py # Experiments with APIs
├── calculator.py # Simple calculator implementation
├── conditions.py # Loops and conditional statements
├── exception.py # Exception handling with try/except
├── libraries.py # Trying different Python libraries
├── loops.py # Loops practice
├── mario.py # Small Python project or exercise
├── name.csv # CSV file used in readCSV.py
├── name.txt # Text file used in exercises
├── openFunction.py # Functions practice
├── readCSV.py # Reading and processing CSV files
├── weather.py # Example with APIs or external data
└── README.md # This file
```
## Concepts Learned

Through this project, I have practiced and explored the following Python concepts:

### Basic String Operations
- Lowercase and uppercase text conversion
- `strip()` to remove whitespace
- `title()` to format text
- Calculating length using `len()`

### Output Formatting
- Using **f-strings** for formatted output

### Core Python Concepts
- Creating and calling **functions**
- Using **loops** (`for`, `while`)
- Conditional statements (`if`, `elif`, `else`)
- Exception handling with `try` and `except`

### Practical Projects
- **Simple Calculator**: Implemented a calculator that performs basic arithmetic operations
- **CSV Handling**: Reading and processing CSV files using Python libraries

### Exploring Python Libraries
- Tried different Python libraries to understand their usage and functionality
- Learned how to interact with **APIs** and work with external data sources

## How to Use

1. Clone the repository:

```bash
git clone https://github.com/mtalharashid/python
```

2. Navigate to the project folder:
```
cd python-learning-project
```

3. Run any Python file to explore the code:
```
python calculator.py
```
```
Regular Expressions (Regex)
In this project, I explored Regular Expressions (Regex), a powerful tool for pattern matching in strings. Regex helps to validate, search, and manipulate text in Python.

Use Cases in This Project

Validating Twitter Handles
```
## Validate Twitter link
Ensured that Twitter usernames follow the correct format, e.g., starting with @ and containing only allowed characters.
Example
```
import re
url = input("twitter url? ").strip()
username = re.sub(r"^(https?://)?(www\.)?twitter\.com/", "", url)
print(f"username: {username}")

```

## Validating Emails
Checked if user emails are valid before saving or processing them.

Example:
```
import re
email_pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
if re.match(email_pattern, "example@gmail.com"):
    print("Valid Email")
else:
    print("Invalid Email")
```

## Checking Customer Usernames

Ensured that customer usernames meet specific rules (like no spaces or special characters).

Example:
```
import re
if re.search(r".+@.+\.", email):
    print("valid")
else:
    print("invalid")
```