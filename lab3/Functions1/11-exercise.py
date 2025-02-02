def is_palindrome(s):
    s = s.replace(" ", "").lower() 
    return s == s[::-1]

text = input("Enter a word or phrase: ")

if is_palindrome(text):
    print(f"Yes, '{text}' is a palindrome!")
else:
    print(f"No, '{text}' is not a palindrome.")
