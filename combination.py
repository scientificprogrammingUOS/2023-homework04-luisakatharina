import numpy as np 

#Write a function `combination` that takes in two numpy arrays and an optional parameter `axis` which should be 0 by default.
#Remove unnecessary dimensions of the input arrays, check whether they can be combined along the given axis and return the combined array.
#If the combination is not possible, raise a meaningful error message.


def combination(arr1, arr2, axis=0):
    #Remove unnecessary dimensions of the input arrays
    arr1 = np.squeeze(arr1)
    arr2 = np.squeeze(arr2)

    # Check whether the arrays can be combined along the given axis
    try:
        combined = np.concatenate((arr1, arr2), axis=axis)
    except ValueError as e:
        raise ValueError(f"Arrays cannot be combined along axis {axis}.") from e

    return combined



if __name__ == "__main__":
    arr1 = np.array([[1, 2], [3, 4]])
    arr2 = np.array([[5, 6], [7, 8]])
    combined = combination(arr1, arr2, axis=1)
    print(combined) 
