def argmax(items):
    m = 0
    arg_m = 0
    for i, item in enumerate(items):
        if item > m:
            m = item
            arg_m = i
    return arg_m
