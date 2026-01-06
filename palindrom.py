def is_palindrome(word):

    word = word.lower()
    word = ''.join(c for c in word if c.isalnum())
    return word == word[::-1]

user_input = input("Adj meg egy szót vagy kifejezést: ")

if is_palindrome(user_input):
    print("Ez a szó palindrom!")
else:
    print("Ez a szó NEM palindrom.")

# róbert:
def is_palindrome(s):
    s = s.replace(' ','')
    return s == s[::-1]
print(is_palindrome('legel'))
print(is_palindrome('geza kek az eg'))