# Validating Postal code
import re

print('Give the 6 digit postal code: ')
P = input()

regex_integer_in_range = r'^[1-9][\d]{5}$'
regex_alternating_repetitive_digits_pair = r'(\d)(?=\d\1)'

print(bool(re.match(regex_integer_in_range, P)) and
      len(re.findall(regex_alternating_repetitive_digits_pair, P)) < 2)
