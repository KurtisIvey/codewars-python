def vowel_count(str):
    vowels = ['a', 'e', 'i', 'o', 'u']
    count = 0
    # lowercase to not be case sensitive & count
    for char in str.lower():
        if char in vowels:
            count += 1
    return count

print(vowel_count('hellosteEw'))