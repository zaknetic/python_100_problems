#Write a Python program that takes two strings as input and concatenates them into a single string without using the `+` operator.

# Method 1: Using join()
def concatenate_using_join(str1, str2):
    return ''.join([str1, str2])

# Method 2: Using a list
def concatenate_using_list(str1, str2):
    result = []
    result.append(str1)
    result.append(str2)
    return ''.join(result)

# Main program
if __name__ == "__main__":
    string1 = input("Enter the first string: ")
    string2 = input("Enter the second string: ")
    
    # Concatenate using join
    concatenated1 = concatenate_using_join(string1, string2)
    print("Concatenated string using join():", concatenated1)
    
    # Concatenate using list
    concatenated2 = concatenate_using_list(string1, string2)
    print("Concatenated string using list:", concatenated2)
