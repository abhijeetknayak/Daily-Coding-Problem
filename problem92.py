
def remove_key(dict, key): # Removing a key from 'values' of other keys
    for k in dict:
        if key in dict[k]:
            dict[k].remove(key) # Removing it from the list

def process_dictionary(dict):
    course_order = []
    key_remove_list = []

    while len(dict) > 0:
        for key in dict: # Iterating over all available keys in the dictionary
            if len(dict[key]) == 0: # Trigger to remove key
                course_order.append(key) # Updating Course Orders
                key_remove_list.append(key) # Keys to be removed from the Dict. Cannot remove it here
                remove_key(dict, key)

        for key_to_remove in key_remove_list: # Removing Key from the Dictionary
            if key_to_remove in dict:
                dict.pop(key_to_remove)

    return course_order

if __name__ == '__main__':
    courses = {"C3": ["C2", "C1"], "C2": ["C1"], "C1": [], "C5": ["C1", "C3", "C4", "C6"], "C4": ["C3", "C6"], "C6": []}
    course_order = process_dictionary(courses)

    print(course_order)
