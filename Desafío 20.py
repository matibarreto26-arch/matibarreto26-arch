# Desafío 20: Caracteres ASCII
# Programa que convierte números ASCII en caracteres

# Pedimos al usuario que ingrese varios números separados por coma
entrada = input("Ingresa números ASCII separados por coma: ")

# Separamos la entrada en una lista
lista_numeros = entrada.split(",")

# Recorremos cada dato ingresado
for elemento in lista_numeros:

    # Quitamos espacios en blanco
    elemento = elemento.strip()

    # Verificamos si el dato ingresado es un número
    if elemento.isdigit():

        # Convertimos el dato a número entero
        numero = int(elemento)

        # Verificamos si está dentro del rango ASCII estándar
        if numero >= 0 and numero <= 127:

            # Convertimos el número a carácter
            caracter = chr(numero)

            # Mostramos el resultado
            print(f"{numero} = {caracter}")

        else:
            print(f"{numero} no está dentro del rango ASCII estándar.")

    else:
        print(f"'{elemento}' no es un número válido.")