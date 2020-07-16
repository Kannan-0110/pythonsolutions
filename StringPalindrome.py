isPalindrome(message):
    if message==message[::-1]:
        print("The String is palindrome")
    else:
        print("The String is not palindrome")

message=input("Enter the string: ")
isPalindrome(message)
