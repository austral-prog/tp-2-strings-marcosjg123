def rectangle():
    """Lee base y altura de un rectángulo, calcula e imprime
    el área y el perímetro.
    """
    base = int(input("Base: "))
    altura = int(input("Altura: "))
    area = base * altura
    perimetro = (2*base) + (2*altura)
    print(f"Area: {area}")
    print(f"Perimetro: {perimetro}")
    pass
rectangle()
