import numpy as np

'''
You come across this strange pattern.

| x     |       |       | x     |       |       | x     |       |
| ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- |
|       |       | **x** |       |       | **x** |       |       |
|       | **x** |       |       | **x** |       |       | **x** |
| **x** |       |       | **x** |       |       | **x** |       |
|       |       | **x** |       |       | **x** |       |       |
|       | **x** |       |       | **x** |       |       | **x** |

Mesmerized, you decide you must write a function to generate arbitrary sizes of it. (_Write a function `strange_pattern` that takes
a shape tuple `(n, m)` as input and generates a boolean (True for x's and False for blank spaces) 2D NumPy array of the given 
shape with this pattern_)
**Hint:** Perhaps this strange symbol might help? `::`
shape tuple: tuple of integers that specifies the dimensions of a multi-dimensional array or matrix
'''

def strange_pattern(tup):
    '''
    True values for x's and False values for blank spaces
    '''
    #create array
    pattern_arr = np.zeros((tup[0],tup[1]), dtype= bool)

    pattern_arr[::3, ::3] = 1
    pattern_arr[1::3, 2::3] = 1
    pattern_arr[2::3, 1::3] = 1

    
    return pattern_arr

if __name__ == "__main__":
    n = 6
    m = 8
    pattern = strange_pattern((6,8))
    print(pattern)


```bash
git add .
```

```bash
git commit -m "Commit message"
```

```bash
git push