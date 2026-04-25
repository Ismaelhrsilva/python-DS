from array2D import slice_me
family = [[1.80, 78.4],
[2.15, 102.7],
[2.10, 98.5],
[1.88, 75.2]]
print(slice_me(family, 0, 2))
print(slice_me(family, 1, -2))

# caso com erro (listas de tamanhos diferentes)
family_bad = [
    [1.80, 78.4],
    [2.15],              # erro aqui
    [2.10, 98.5]
]

print(slice_me(family_bad, 0, 2))
