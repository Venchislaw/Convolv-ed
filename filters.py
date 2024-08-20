import numpy as np
# File with convolution filters

def verticle_edges(size=(3, 3), left_values=-1, right_values=1):
    kernel = np.zeros(size)
    kernel[:, 0] = left_values
    kernel[:, -1] = right_values

    return kernel

def horizontal_edges(size=(3, 3), upper_values=1, lower_values=-1):
    kernel = verticle_edges(size=size[::-1]).T
    return kernel

def sharpen(size=(3, 3), central_value=1.4, surrounding_values=-0.05):
    kernel = np.full(size, surrounding_values)
    kernel[kernel.shape[0] // 2, kernel.shape[1] // 2] = central_value
    return kernel

def blur(size=(3, 3)):
    size = np.array(size)
    print(size.size)
    kernel = np.full(size, 1 / np.prod(size))
    return kernel


def gaussian_blur(size=(3, 3)):
    kernel = np.random.normal(size=size, scale=1)
    return kernel
