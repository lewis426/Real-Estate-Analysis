def mean(data):
    count = 0
    total = 0
    for x in data:
        count += 1
        total += x
    return total / max(1, count)

