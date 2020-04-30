#!/usr/bin/python3
import hidden_4
_list = dir(hidden_4)
for i in range(len(_list)):
    if _list[i][0] != "_":
        print('{}'.format(_list[i]))
