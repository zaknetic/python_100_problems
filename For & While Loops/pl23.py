#Write a Python program using a while loop to count
#  the number of digits in a given integer N.


def count_digits(N):
    N = abs(N)

    if N == 0:
        return 1
    
    count = 0
    while N > 0:
        N//=10
        count += 1
    return count

number = int(input("Enter an integer: "))
digit_count = count_digits(number)
print(f"The number of digits in {number} is: {digit_count}")