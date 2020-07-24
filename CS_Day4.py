# Palindrome detector 
import string 

# Read input phrase
phrase = input("Please type a phrase: ")

#Convert to lower case and replace white spaces
phrase = phrase.lower()
phrase = phrase.replace(' ','')

# Replace each special character
for c in string.punctuation: 
  phrase = phrase.replace(c, '')

# Finally check if the result is equal to itself in 
# reverse. 
print(phrase)
if phrase == phrase[::-1]: 
  print("This is a palindrome")
else: 
  print("This is not a palindrome")

