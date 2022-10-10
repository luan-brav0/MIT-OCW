import itertools

word = 'bust'
i = 0
perms = []
letter_perm = list(itertools.permutations(list(word)))

for w in range(len(letter_perm)):
    perms.append(''.join(letter for letter in letter_perm[w]))
print(perms)
l = ['a', 'b', 'c'] 
print()       