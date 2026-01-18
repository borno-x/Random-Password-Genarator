"""
Author: Borno Modak (borno-x)
Created: 18-Jan-2026
Last Modified: 18-Jan-2026
Description: Random password generator
"""

import random
import string

def generate_password(length=12):
    
    characters = string.ascii_letters + string.digits + string.punctuation
 
    password = ''.join(random.choice(characters) for _ in range(length))
    return password


new_password = generate_password()
print("Your new password is:", new_password)