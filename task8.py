import re

# Read file contents
with open('file.txt', 'r') as file:
    content = file.read()

# Extract email addresses using regex
email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
emails = re.findall(email_pattern, content)

# Print the extracted emails
print(emails)
