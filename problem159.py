if __name__ == '__main__':
    str = 'aAbhijeet' # String
    recurring_char = None

    dict = {}

    for char in str.lower():
        if char in dict: # Already available. Recurring character. Exit
            recurring_char = char
            break
        else:
            dict[char] = 1 # Initializing the char in the Dictionary
    print(recurring_char)