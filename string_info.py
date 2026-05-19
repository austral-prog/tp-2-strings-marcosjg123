def string_info():
    """Dada la palabra 'Programacion', imprime su longitud, primera y última letra,
    la palabra repetida 3 veces y decorada con '***'.
    """
    palabra = "Programacion"
    completa = (palabra[:])
    longitud = (len(palabra))
    primer = (palabra[0])
    ultima = (palabra[-1])
    repetida = (palabra*3)
    decora = (f"***{palabra}***")
    print(f"Palabra: {completa}")
    print(f"Longitud: {longitud}")
    print(f"Primera Letra: {primer}")
    print(f"Ultima Letra: {ultima}")
    print(f"Repetida: {repetida}")
    print(f"Decorada: {decora}")
string_info()
