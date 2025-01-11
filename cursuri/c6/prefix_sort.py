def prefix_comun(s):
    def p_max(t):
        for i in range(len(s), 0, -1):
            if t.startswith(s[:i]):
                return i
        return 0
    return p_max

L = ["apasator", "apartament", "exemplu", "ars", "test",
"aparat", "amic"]
s = "aparator"

S = sorted(L, key = prefix_comun(s), reverse=True)
print(*S, sep="\n")