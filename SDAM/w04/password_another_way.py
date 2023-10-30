from getpass import getpass
import random
import sys
import time

pwd = input("Enter your password: ")
def password(pwd, attempts=5):
    for attempts_remaining in reversed(range(attempts)):
        prompt='Please enter your password ({} attempts remaining): '.format(attempts_remaining + 1)
        entry = getpass(prompt=prompt)

        print('Please wait...')

        time.sleep(random.uniform(0.5, 1))

        if entry == pwd:
            print('Correct, logging in.')
            return True
        else:
            print('Incorrect password.')
    return False

if __name__ == '__main__':
    if password(pwd):
        print('Login successful.')
    else:
        print('Closing program.')
        sys.exit(-1)