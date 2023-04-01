


def menu():
    print('Bienvenido al sistema de matrícula de estudiantes')
    print('Por favor, seleccione una opción:')
    print('1. Matricular estudiante')
    print('2. Registrar materia')
    print('3. Ver lista de estudiantes matriculados')
    print('4. Ver lista de materias registradas')
    print('5. Asignar materia a estudiante')
    print('6. Cancelar materia')
    print('7. Quitar la matrícula del estudiante')
    print('8. Salir')
    
while True:#Este menú utiliza un bucle while para que el usuario pueda seleccionar opciones una y otra vez hasta que decida salir del programa.
    menu()
    opcion = input('Ingrese el número de la opción que desea seleccionar: ')
    if opcion == '1':
        # Lógica para matricular estudiante
        print('Ha seleccionado la opción de matricular estudiante.')#elif condicon adicional Si selecciona la opción "2" Lógica para registrar materia
    elif opcion == '2':
        
        print('Ha seleccionado la opción de registrar materia.')
    elif opcion == '3':
        # Lógica para ver lista de estudiantes matriculados
        print('Ha seleccionado la opción de ver lista de estudiantes matriculados.')
    elif opcion == '4':
        # Lógica para ver lista de materias registradas
        print('Ha seleccionado la opción de ver lista de materias registradas.')
    elif opcion == '5':
        # Lógica para asignar materia a estudiante
        print('Ha seleccionado la opción de asignar materia a estudiante.')
    elif opcion == '6':
        # Lógica para cancelar materia
        print('Ha seleccionado la opción de cancelar materia.')
    elif opcion == '7':
        # Lógica para quitar matrícula del estudiante
        print('Ha seleccionado la opción de quitar la matrícula del estudiante.')
    elif opcion == '8':
        print('Gracias por usar el sistema de matrícula. ¡Hasta pronto!')
        break
    else:##else se utiliza en una estructura de control de flujo para especificar un bloque de código que se ejecuta cuando la condición de una instrucción if es False
        print('Opción no válida. Por favor, seleccione una opción del 1 al 8.')









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

