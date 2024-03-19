
def multiples_less_than(n, limit):
    multiples = set()
    for num in n:
        for i in range(1, limit):
            if i % num == 0:
                multiples.add(i)
    return len(sorted(multiples))
def Three_four_three():
    tft = set()
    for a in range(1,10):
        for b in range(10):
            for c in range(10):
                if (a + b + c) % 2 == 0:
                    n = a*100 + b*10 + c
                    tft.add(n)
    return sorted(tft)


limit = 1000
print(Three_four_three())
print(len(Three_four_three()))
