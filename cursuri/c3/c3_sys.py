import sys
s = "test"
x = "st"
t = sys.intern("te" + x)
print(s == t)
print(s is t)