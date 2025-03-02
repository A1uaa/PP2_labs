s = input().lower().replace(" ", "")
is_palindrome = s == ''.join(reversed(s))

print("Palindrome:", is_palindrome)
