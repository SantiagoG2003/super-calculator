playing = True

while playing:
    num1 = int(input("Ingresa el número 1:"))
    num2 = int(input("Ingresa el número 2:"))

    print("Ingresa la operacion que deseas hacer:")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Salir")

    user_input = int(input())

    if user_input == 1:
        suma = num1+num2
        print("La suma es...", suma)
    elif user_input == 2:
        print("La resta es...")