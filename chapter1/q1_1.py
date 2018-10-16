import hashtable

def has_unique_chars(input_string):
    charMap = hashtable.HashTable(27)
    for char in input_string:
        if char is ' ':
            continue
        if charMap.get(char) is not False:
            return False
        else:
            charMap.put(char, 1)
    return True
