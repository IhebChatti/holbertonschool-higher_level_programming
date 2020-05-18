#!/usr/bin/python3
def safe_function(fct, *args):
    import sys
    try:
        ret = fct(args[0], args[1])
        return ret
    except Exception as e:
        print('Exception: {}'.format(e), file=sys.stderr)
        return None
