from numpy import round

cats = {
    'a': 0,
    'b': 0,
    'c': 0,
    'd': 0,
    'e': 0
}
stream = ['a', 'b', 'c', 'a', 'd', 'e', 'a', 'c', 'b', 'b']

c = 0.1
u = 0.6

for s in stream:
    for cat in cats:
        b = 1 if s == cat else 0 # bit

        val = round(cats[cat] * (1 - c) + b, decimals=3)
        cats[cat] = 0 if val < u else val

print(cats)