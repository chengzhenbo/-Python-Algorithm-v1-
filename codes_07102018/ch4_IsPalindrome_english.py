def is_palindrome(s):
    if len(s) <= 1:
        return True
    else:
        return s[0] == s[-1] and is_palindrome(s[1:-1])
if __name__ == '__main__':
    s = "noon"
    if(is_palindrome(s)):
        print("\""+s+"\""+" is a palindrome!")
    else:
        print("\""+s+"\""+" is not a palindrome!")