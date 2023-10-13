wishes = ["I love you",
            "a little",
            "a lot",
            "passionately",
            "madly",
            "not at all",
            ]

petals = int(input('amount of petals: '))

for petal in range(petals):
    index = petal%len(wishes)
    last_wish = wishes[petal%len(wishes)]

print(last_wish)
print(index)