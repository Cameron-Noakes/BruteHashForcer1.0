import hashlib

#AUTHOR: Cameron Noakes
# This program will take a hash value (stored in hash_to_crack) and compare a list
# of passwords to the decoded hash value, this is done by md5 encoding the passlist
# and then comparing the hash values to determine if a crack can occur through the
# password list provided. If both the md5 encoded password in the list and the actual
# hash value match then it is successful at guessing the hash value, if not it will
# break out of the loop and display an output termination message saying the brute
# force crack attempt failed.

# Hash to be cracked
hash_to_crack = "5f4dcc3b5aa765d61d8327deb882cf99"

# List of possible passwords
password_list = ["password", "123456", "qwerty", "letmein", "monkey"]

# Iterate through the list of possible passwords
for password in password_list:
    # Hash the current password
    hashed_password = hashlib.md5(password.encode()).hexdigest()
    # Compare the hashed password with the hash to be cracked
    if hashed_password == hash_to_crack:
        print(f"Password found: {password}")
        break
else:
    print("Password not found in the list.")
