# Write a Python program that takes a single character
# as input and determines whether it is a vowel or a consonant.

def check_char(char):
    vowels = 'aeiouAEIOU'
    return char in vowels

def main():
    char = input("Enter a single character: ")

    if len(char) != 1 or not char.isalpha():
        print("Please enter a single alphabetic character.")

    else:
        if check_char(char):
            print(f"{char} is a vowel.")
        else:
            print(f"{char} is a consonant.")

if __name__ == "__main__":
    main()