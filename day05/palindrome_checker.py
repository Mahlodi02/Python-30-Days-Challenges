# Palindrome Checker

def palindrome(x: str) -> bool:
    if x == x[::-1]:
        return True
    else:
        return False
    
print(palindrome("1441"))
