#! python
# An insecure password manager
import sys
import pyperclip

passwords = {'email': 'F7minlBDDuvMJuxESSKHFhTxFtjVB6',
             'blog': 'VmALvQyKAxiVH5G8v01if1MLZF3sdt',
             'luggage': '12345'}

# Conditional Check
if len(sys.argv) < 2:
    print('Usage: python password_manager.py [account] - copy account password')
    sys.exit()

account = sys.argv[1]  # First command line argument is the account name

# Copy password to clipboard if in passwords
if account in passwords:
    pyperclip.copy(passwords[account])
    print(f'Password for {account} copied to clipboard.')
else:
    print(f'There is no account named {account}')
