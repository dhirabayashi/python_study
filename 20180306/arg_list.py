def write_multiple_items(file, separator, *args):
    file.write(separator.join(args))


with open("test.txt", "w") as f:
    write_multiple_items(f, ",", "a", "b", "c")


def concat(*args, sep="/"):
    return sep.join(args)


print(concat("earth", "mars", "venus"))
print(concat("earth", "mars", "venus", sep="."))
