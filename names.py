def names():
    """Lee nombre y apellido, e imprime el nombre completo en distintos formatos:
    minúsculas, título, mayúsculas y con tabulador.
    """
    opening = input("Ingresa tu nombre:")
    print(opening.lower())
    print(opening.title())
    print(opening.upper())
    print("\t" + opening.lower())
    pass
names()
