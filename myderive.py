#!/usr/bin/env python3

def myderive(f, var):
    if type(f) == str:
        if f == var:
            return 1
        else:
            return 0
    elif type(f) == list:
        if f[0] == "+":
            return ["+", myderive(f[1], var), myderive(f[2], var)]
        if f[0] == "-":
            return ["-", myderive(f[1], var), myderive(f[2], var)]
        if f[0] == "*":
            return ["+", ["*", myderive(f[1], var), f[2]], ["*", f[1], myderive(f[2], var)]]
        if f[0] == "/":
            return ["/", ["-", ["*", myderive(f[1], var), f[2]], ["*", f[1], myderive(f[2], var)]], ["*", f[2], f[2]]]
    else:
        return 0
