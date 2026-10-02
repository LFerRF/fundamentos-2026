def calculadora_inteligente():
    saludo = input("digita tu nombre: ")
    print(f"Hola! {saludo} que quieres hacer hoy?")
    
    operacion = input("---> ")
    if operacion == "suma":
        suma = int(input("numero 1: ")) + int(input("numero 2: "))
        return suma
    elif operacion == "resta":
        resta = int(input("numero 1: ")) - int(input("numero 2: "))
        return resta
    elif operacion == "multiplicacion":
        Producto = int(input("numero 1: ")) * int(input("numero 2: "))
        return Producto
    elif operacion == "division":
        division = int(input("numero 1: ")) / int(input("numero 2: "))
        return division

print(calculadora_inteligente())