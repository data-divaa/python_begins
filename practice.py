import re

def color_code(code):
    # Corrected the regex to match either 3 or 6 digit hex color codes
    ex = r"(#[0-9a-fA-F]{3}|#[0-9a-fA-F]{6})(?=[^a-zA-Z0-9-])"
    result = []

    for i in code:
        match = re.findall(ex, i)
        if match:
            result.extend(match)  # Use match.group() to get the matched string

    for k in result:
        print(k)

# Get the number of lines
n = int(input("Enter the number of lines of code: "))
code = [input() for _ in range(n)]  # Collect input lines
color_code(code)
