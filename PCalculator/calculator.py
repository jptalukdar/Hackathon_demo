def add(*args):
    """
    Allows you to add numbers
    Args:
        *args: variable parameters
    """
    sum = 0
    for arg in args:
        if type(arg) == str:
            try:
                arg=float(arg)
            except :
                continue
        sum += arg

    return sum

 
