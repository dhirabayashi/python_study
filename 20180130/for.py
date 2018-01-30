animals = ['cat', 'bear', 'giraffe']

for animal in animals[:]:
    if len(animal) > 5:
        animals.insert(0, animal)
        print(animals)
