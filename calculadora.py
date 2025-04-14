def menu():
    print("\n=== Calculadora en Python ===")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")
    print("5. Salir")
    return input("Elige una opción: ")

def obtener_valor(mensaje):
    while True:
        valor = input(mensaje + " (! para volver): ")
        if valor == "!":
            return "!"
        try:
            return float(valor)
        except ValueError:
            print("Por favor, ingresa un número válido o '!' para volver.")

def formatear_numero(num):
    return int(num) if num.is_integer() else num

def mostrar_resultado(operacion, num1, num2, resultado):
    num1 = formatear_numero(num1)
    num2 = formatear_numero(num2)
    resultado = formatear_numero(resultado)
    print(f"\n{operacion} de {num1} y {num2} = {resultado}")
    input("Ingresa X para volver al menú principal: ")

def calculadora():
    while True:
        opcion = menu()
        
        if opcion == "5":
            print("Gracias por usar la calculadora. ¡Hasta pronto!")
            break
        elif opcion in ["1", "2", "3", "4"]:
            num1 = obtener_valor("Ingresa el primer número")
            if num1 == "!":
                continue
            num2 = obtener_valor("Ingresa el segundo número")
            if num2 == "!":
                continue

            if opcion == "1":
                resultado = num1 + num2
                operacion = "Suma"
            elif opcion == "2":
                resultado = num1 - num2
                operacion = "Resta"
            elif opcion == "3":
                resultado = num1 * num2
                operacion = "Multiplicación"
            elif opcion == "4":
                if num2 == 0:
                    print("Error: No se puede dividir por cero.")
                    continue
                resultado = num1 / num2
                operacion = "División"

            mostrar_resultado(operacion, num1, num2, resultado)
        else:
            print("Opción no válida. Intenta nuevamente.")

calculadora()