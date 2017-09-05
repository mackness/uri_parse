"""uriparse utils file"""

def is_int(integer):
    """return boolean based on weather or not param integer is type int"""
    val = None

    try:
        val = int(integer)
    except ValueError:
        pass

    if val:
        return True
    else:
        return False

    return val
