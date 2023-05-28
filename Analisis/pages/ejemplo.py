import numpy as np

def array_product(str1, str2):
    # Convert strings to NumPy arrays
    array1 = np.fromstring(str1, dtype=float, sep=' ')
    array2 = np.fromstring(str2, dtype=float, sep=' ')

    # Calculate the element-wise product
    product = np.matmul(array1, array2)

    return product

# Example usage
string1 = "1 2 3 4 5"
string2 = "6 7 8 9 10"
result = array_product(string1, string2)

print("Product:", result)