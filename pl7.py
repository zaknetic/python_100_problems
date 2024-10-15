#Write a Python function to check if a given string is a palindrome or not.


input_str = 'civic'
rev = input_str[::-1]

if input_str == rev:
    print(rev," is Palindrome")
else:    
    print(rev," is not Palindrome")