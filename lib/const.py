def solve(s):
    def get_consonant_value(substring):
        return sum(ord(char) - ord('a') + 1 for char in substring)

    vowels = "aeiou"
    consonant_substrings = [substring for substring in s.split(vowels) if substring]

    if not consonant_substrings:
        return 0  # No consonants in the string

    max_value = max(get_consonant_value(substring) for substring in consonant_substrings)
    return max_value

print(solve("zodiacs"))    # Output: 26
print(solve("strength"))   # Output: 57
