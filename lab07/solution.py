import numpy as np

def reshape_rows(values, width):
    if width <= 0 or len(values) % width != 0:
        return []

    values = np.asarray(values, dtype=float)
    values = values.reshape(-1,width)

    return values.tolist()

def block(matrix, rows, columns):
    arr = np.asarray(matrix, dtype=float)

    result = arr[np.ix_(rows, columns)]

    return result.tolist()

def column_means(matrix):
    if len(matrix) == 0: return []

    arr = np.asarray(matrix, dtype=float)

    result = np.mean(arr, axis=0)

    return np.round(result, 6).tolist()

def column_range(matrix, column):
    if len(matrix) == 0:
        return 0.0

    arr = np.asarray(matrix, dtype=float)

    result = np.max(arr[:, column]) - np.min(arr[:, column])

    return float(round(result, 6))

