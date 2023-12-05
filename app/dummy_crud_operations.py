
"""Dummy_CRUD_operations.py
This is just a dummy demontstarion of CRUD Operations on a file.
Modifications needed as per db

"""

# Create a new file and write to it
file = open('dummy.txt', 'w')
file.write('This file is for testing CRUD Operations.')
file.close()

# Read data from a file
file = open('dummy.txt', 'r')
content = file.read()
print(content)
file.close()

# Update data in a file
file = open('dummy.txt', 'w')
file.write('This is the updated data in the file.')
file.close()

# Delete a file
import os
os.remove('dummy.txt')
