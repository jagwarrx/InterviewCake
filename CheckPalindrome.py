def has_palindrome_permutation(the_string):

    # Check if any permutation of the input is a palindrome
    chars = set()
    for char in the_string:
        if char not in chars:
            chars.add(char)
        else:
            chars.remove(char)
    return len(chars) <= 1
