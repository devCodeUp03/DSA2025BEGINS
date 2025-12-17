s = "babad"
substrings = [s[i:j] for i in range(len(s)) for j in range(i+1, len(s) + 1)]


def check_palindrome(substring):
    orginal = substring
    reverse = substring[::-1]

    return True if orginal == reverse else False

array_of_palindrome = []
for ss in substrings:
    is_palindrome = check_palindrome(ss)
    if is_palindrome:
        array_of_palindrome.append(ss)

mp_of_palindromes = {}

for ss in array_of_palindrome:
    mp_of_palindromes[ss] = len(ss)

longest_palindrome = max(mp_of_palindromes, key=mp_of_palindromes.get)


print(longest_palindrome)
