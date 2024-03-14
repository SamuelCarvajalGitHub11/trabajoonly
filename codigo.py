def suma_numeros():
    try:
        # Solicitar al usuario que ingrese los números
        num1 = float(input("Ingresa el primer número: "))
        num2 = float(input("Ingresa el segundo número: "))

        # Calcular la suma
        suma = num1 + num2

        # Mostrar el resultado
        print("La suma de", num1, "y", num2, "es:", suma)
    except ValueError:
        print("Error: Ingresa números válidos.")

# Llamar a la función para sumar números
suma_numeros()
