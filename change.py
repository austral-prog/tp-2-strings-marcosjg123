def change():
    """Lee un gasto y el dinero recibido, calcula el vuelto
    y lo separa en pesos (parte entera) y centavos.
    """
    gasto = float(input("Ingresar Gasto:"))
    dinero_recibido = int(input("Dinero Recibido:"))
    print(gasto)
    print(dinero_recibido)
    vuelto = dinero_recibido-gasto
    pesos = int(vuelto)
    centavos = int((vuelto - pesos)*100)
    print(pesos)
    print(centavos)

    pass
change()
