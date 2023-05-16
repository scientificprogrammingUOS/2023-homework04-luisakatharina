import numpy as np

'''
Write a function `gaussian_analysis` which takes four parameters `loc`, `scale`, `lower_bound` and `upper_bound` and returns a tuple 
of two values (`mean`, `std`).
First of all the function should make sure that `loc`, `scale`, `lower_bound` and `upper_bound` are integers or floats and 
that `lower_bound` is smaller than `upper_bound` and should return meaningful error messages if those are not the case.
In the function 100 samples of a gaussian distribution should be drawn in respect to the given `loc` and `scale` parameters. 
Check out the Numpy documentation to find out which function you could use here.
Next, the values below the `lower_bound` and above the `upper_bound` should be filtered out. Afterwards you should 
calculate the `mean` and the `std`(standard deviation) of the array and return them in a tuple.
'''


def gaussian_analysis(loc, scale, lower_bound, upper_bound):
    # Check input types and bounds
    if not all(isinstance(param, (int, float)) for param in [loc, scale, lower_bound, upper_bound]):
        raise TypeError("All parameters must be integers or floats.")
    if lower_bound >= upper_bound:
        raise ValueError("Lower bound must be smaller than upper bound.")

    # Draw 100 samples from the Gaussian distribution
    samples = np.random.normal(loc=loc, scale=scale, size=100)

    # Filter out samples outside the bounds
    in_bounds = samples[(samples >= lower_bound) & (samples <= upper_bound)]

    # Compute mean and standard deviation of the filtered samples
    mean, std = np.mean(in_bounds), np.std(in_bounds)

    return mean, std


if __name__ == "__main__":
    mean, std = gaussian_analysis(0, 1, -1, 1)
    print(f"Mean: {mean}, Std: {std}") 

