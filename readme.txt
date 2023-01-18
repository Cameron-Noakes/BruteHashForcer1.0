BruteHashForcer - README.txt

#AUTHOR: Cameron Noakes
This script will iterate through the list of possible passwords, 
hash each one using the MD5 algorithm (as specified by the hashlib.md5() 
function), and compare the resulting hash value to the hash to be cracked. 
If a match is found, the script will print the matching password and exit. 
If the loop completes without finding a match, the script will print a 
message indicating that the password was not found in the list.

