def generator():
    for e in range(1, 20):
        yield e


gen = generator()

# for e in range(1, 10):
#     print(next(gen))

# for e in generator():
#     print(e)

# CICLO WHILE
gen = generator()
while gen:
    try:
        value = next(gen)
        print(value)
    except StopIteration as si:
        print('Se acabo de consumir el generator')
        break
