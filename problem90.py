import numpy as np

def return_actual_values(list, n): # Excluding values in the list from what we generate
    val_list = []
    for value in range(0, n):
        if value not in list: val_list.append(value)
    return val_list # Final values that need to be generated

def generate(num_samples, n,  list):
    rand_num = 0
    dict = {}
    final_values = return_actual_values(list, n)
    for k in range(0, num_samples):
        # for i in range(0, len(val)):
        #     rand_num += np.random.randint(0, len(val))
        # rand_num = rand_num % len(val)
        rand_num = np.random.randint(0, len(final_values)) # Generating random indices
        final_val = final_values[rand_num]

        if final_val in dict: # Updating Dictionary of values already seen
            dict[final_val] += 1
        else:
            dict[final_val] = 1

    for key in dict:
        dict[key] /= num_samples # Occurance Percentage over all samples
    print(dict)


if __name__ == '__main__':
    num_samples = 100000 # Number of measurements
    n = 10

    list = [1, 3, 5] # Exclude values

    generate(num_samples, n, list)


