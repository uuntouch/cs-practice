def count_items(values):
    counts = {}

    for item in values:
        counts[item] = counts.get(item, 0) + 1

    return counts

def unique_sorted(values):
    return sorted(set(values))

def common(first, second):
    arr = []
    for i in first:
        if i in second and i not in arr:
            arr.append(i)

    return sorted(arr)

def only_in_first(first, second):
    arr = []
    for i in first:
        if i not in second and i not in arr:
            arr.append(i)

    return sorted(arr)