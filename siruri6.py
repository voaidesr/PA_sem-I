def op(s, t):
    if s == "" or t == "":
        return s + t
    if s[-1] != t[0]:
        return s + t
    else:
        c = t[0]
        s = s.rstrip(c)
        t = t.lstrip(c)
        return (s,t)
