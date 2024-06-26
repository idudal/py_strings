# pylint:
def reverse(text: str) -> str:   
    """
    Return the 'text' backwards.
    Parameters
    ----------
    text: str
        The input string
    Returns
    -------
    str
        The text written backwards.
    """
    return text[::-1]





def first_to_upper(text: str) -> str:
    words = text.split()
    capitalized_words = [word[0].upper() + word[1:] for word in words]
    return ' '.join(capitalized_words)


def count_vowels(text: str) -> int:
    vowels = "aeiouAEIOUyYęąóĘĄÓ"
    count = 0
    for char in text:
        if char in vowels:
            count += 1
    return count


def sum_digits(text: str) -> int:
    digits = "0123456789"
    suma = 0
    for char in text:
        if char in digits:
            suma += int(char)
    return suma


def search_substr(text: str, sub: str) -> int:
    """
    Search for sub(string) in the text. Returns the position or None.

    Parameters
    ----------
    text: str
        The input string

    Returns
    -------
    int or None
        Position of the sub(string) or None.
    """
    pass
