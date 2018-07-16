from math import pi
from datetime import datetime

# F-Strings are introduced in python 3.6 and really good to use!

first_name = 'Retro'
last_name = 'Metro'
birthday = datetime(1973, 7, 11)

name_log = {'first_name': 'Retro', 'last_name': 'Metro', 'age': 25}

# Indicate 'f' before the quotations
print(f'My name is {first_name} {last_name}')

# Functions with F-Strings!
print(f'My name is {first_name.upper()} {last_name.lower()}')

# F-string with dictionaries
print(f"My name is {name_log['first_name']} {name_log['last_name']} and i am {name_log['age']} years old.")

# Calculations in F-Strings
print(f'20 times 13 is {20*13}')

# Looping with F-Strings with padding, formatting
for i in range(20):
    print(f'Loop number is {i:02}')
    if i >= 5:
        break

# F-String with floating points!
print(f'The value if Pi is {pi:.5f}')

# F-String with datetime objects!
print(f'Retro birthday: {birthday:%B %d, %Y }')
