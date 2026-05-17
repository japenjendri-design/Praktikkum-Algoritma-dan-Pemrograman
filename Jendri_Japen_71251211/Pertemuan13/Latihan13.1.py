def cek_tuple(t):
    return all(x == t[0] for x in t)

tA = (90,90,90,90)
print(cek_tuple(tA))