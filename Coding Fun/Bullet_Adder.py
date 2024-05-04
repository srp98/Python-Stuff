#! python
# Import Libraries
import pyperclip

# Get Clipboard data
text = pyperclip.paste()

# Separate Lines and Add stars
lines = text.split('\n')
for i in range(len(lines)):
    lines[i] = '* ' + lines[i]

# Update text
text = '\n'.join(lines)

# Copy the new text to clipboard
pyperclip.copy(text)
