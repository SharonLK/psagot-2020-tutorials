import numpy as np

if __name__ == '__main__':
    spicy_matrix = np.arange(0, 50).reshape((10, 5))

    print(spicy_matrix)

    # The same as `np.sum(spicy_sums, axis=0)`
    print(spicy_matrix.sum(axis=0))
    print(spicy_matrix.sum(axis=0).shape)

    # The same as `np.sum(spicy_sums, axis=1)`
    print(spicy_matrix.sum(axis=1))
    print(spicy_matrix.sum(axis=1).shape)

    # TODO: Have more fun with numpy
