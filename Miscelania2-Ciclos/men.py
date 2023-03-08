#ver materias registradas cuando el estudiante ingresa
materias = ['Matemáticas', 'Ciencias', 'Historia', 'Idiomas'] #lista materias, materias registradas

def imprimir_materias():#def para definir la funcion imprime la lista de materias en pantalla.
    for i, materia in enumerate(materias):
        print(f"{i+1}. {materia}")

def menu_estudiante():#La función menu_estudiante es el menú que se le presenta al estudiante.
    print("Bienvenido, por favor seleccione una opción:")#Cuando el estudiante ingresa al programa, se le muestra el menú de opciones print. 
    print("1. Ver materias registradas")
    print("2. Salir")

    opcion = input("Ingrese una opción: ")

    if opcion == "1": #Si selecciona la opción "1", se llama a la función imprimir_materias para mostrar la lista de materias.
        imprimir_materias()
        menu_estudiante()
    elif opcion == "2":#elif condicon adicional Si selecciona la opción "2", se cierra el programa.
        print("Gracias por utilizar el programa.")
    else:#else se utiliza en una estructura de control de flujo para especificar un bloque de código que se ejecuta cuando la condición de una instrucción if es False
        print("Opción inválida. Por favor, seleccione una opción válida.")#Si ingresa una opción inválida, se muestra un mensaje de error y se llama a la función menu_estudiante de nuevo para que el estudiante vuelva a seleccionar una opción válida.
        menu_estudiante()

menu_estudiante()