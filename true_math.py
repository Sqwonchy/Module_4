import math

def divide(first,second):
    first = int(first)
    second = int(second)
    if second == 0:
        return math.inf
    else:
        return  first/second
