def ficha():
    """Ejercicio integrador. Lee nombre, email y 3 notas, y genera una ficha
    de alumno aplicando: strip, title, lower, upper, int, len, find, slicing,
    reverse, replace, count, in, f-strings, strings multilínea y operaciones matemáticas.
    """
    # Ejercicio integrador: Generador de Ficha de Alumno
    #
    # Leer mediante input:
    #   1. Nombre completo (puede tener espacios extra y mayúsculas mezcladas)
    #   2. Email (puede tener mayúsculas)
    #   3. Tres notas (como texto, hay que convertirlas)
    #
    # Generar una ficha que incluya:
    #   - Encabezado decorativo usando un string multilínea con "="
    #   - Nombre limpio: sin espacios extra y con formato título
    #   - Email en minúsculas
    #   - Cantidad de caracteres del nombre
    #   - Iniciales: usar find para encontrar el espacio e indexar las letras
    #   - Usuario: apellido.nombre en minúsculas
    #   - Verificar si el email contiene @ 
    #   - Extraer el dominio del email
    #   - Nombre con guion bajo en vez de espacio
    #   - Contar las 'a' en el nombre
    #   - Código secreto: nombre invertido en mayúsculas
    #   - Las 3 notas, su suma, promedio y promedio entero
    #   - Cierre decorativo usando repetición de string ("=" * 24)
    nombre = input("Ingrese Su Nombre: ")
    mail = input("Ingrese Su Mail: ")
    nota1 = input("Ingrese Su 1er Nota:")
    nota2 = input("Ingrese su 2da Nota:")
    nota3 = input("Ingrese Su 3er Nota:")

    nombre_limpio = nombre.strip().title()
    mail_limpio = mail.lower()

    espacio = nombre_limpio.find(" ")
    nombre_solo = nombre_limpio[:espacio]
    apellido = nombre_limpio[espacio + 1:]

    usuario = apellido.lower() + "." + nombre_solo.lower()

    posicion_arroba = mail_limpio.find("@")
    dominio = mail_limpio[posicion_arroba + 1:]

    nota1 = int(nota1)
    nota2 = int(nota2)
    nota3 = int(nota3)

    suma = nota1 + nota2 + nota3
    promedio = suma / 3
    promedio_entero = suma // 3

    print("""========================
    FICHA DEL ALUMNO
========================""")
    print(f"Nombre: {nombre_limpio}")
    print(f"Email: {mail_limpio}")
    print(f"Caracteres en nombre: {len(nombre_limpio)}")
    print(f"Iniciales: {nombre_limpio[0] + nombre_limpio[nombre_limpio.find(' ') + 1]}")
    print(f"Usuario: {usuario}")
    print(f"Email valido: {'@' in mail_limpio}")
    print(f"Dominio: {dominio}")
    print(f"Nombre para archivo: {nombre_limpio.replace(' ', '_')}")
    print(f"Cantidad de a: {nombre_limpio.lower().count('a')}")
    print(f"Codigo secreto: {nombre_limpio[::-1].upper()}")
    print(f"Nota 1: {nota1}")
    print(f"Nota 2: {nota2}")
    print(f"Nota 3: {nota3}")
    print(f"Suma: {suma}")
    print(f"Promedio: {promedio}") 
    print(f"Promedio entero: {promedio_entero}")
    print("=" * 24)
    pass
ficha()
