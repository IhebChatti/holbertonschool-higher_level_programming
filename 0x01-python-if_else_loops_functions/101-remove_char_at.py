#!/usr/bin/python3
def remove_char_at(str, n):
    str_cpy = str
    if len(str_cpy) >= n:
        str_cpy = str[:n] + str[n+1:]
    return(str_cpy)
