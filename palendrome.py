#determine if a given string is a palendrome

def isPalendrome(s):
    return (s == s[::-1])

print isPalendrome(raw_input('enter a string: '))
