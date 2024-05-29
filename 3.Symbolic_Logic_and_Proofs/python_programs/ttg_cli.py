import ttg

#print(ttg.Truths(
#    ['p', 'q', 'r'],
#    ['p => q', 'q => r', '(p => q) or (q => r)'],
#    ints=False)
#)
print(ttg.Truths(
    ['p', 'q', 'r'],
    ['p => (q or r)', 'p => q', 'p => r', '(p => q) or (p => q) or (p => r)'],
    ints=False)
)
#print(ttg.Truths(
#    ['p', 's', 'q','r'],
#    ['p or s', 's => q', '(p or q) => r', '(p or s) and (s => q) and ((p or q) => r)'],
#    ints=False)
#)