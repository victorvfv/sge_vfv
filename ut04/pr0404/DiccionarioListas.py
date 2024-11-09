asignaturas = {
    "Matemáticas": ["Ana", "Carlos", "Luis", "María", "Jorge"],
    "Física": ["Elena", "Luis", "Juan", "Sofía"],
    "Programación": ["Ana", "Carlos", "Sofía", "Jorge", "Pedro"],
    "Historia": ["María", "Juan", "Elena", "Ana"],
    "Inglés": ["Carlos", "Sofía", "Jorge", "María"],
}

def listar_estudiantes(asignatura):
    if asignatura in asignaturas:
        print("Estudiantes en "+asignatura + str(asignaturas.get(asignatura)))
    else:
        print("La asignatura no existe.")

def matricular_estudiante(asignatura, estudiante):
    if asignatura in asignaturas:
        if estudiante not in asignaturas[asignatura]:
            asignaturas[asignatura].append(estudiante)
            print(estudiante + "se ha matriculado en" + asignatura)
        else:
            print(estudiante + "ya está matriculado en" + asignatura)
    else:
        print("La asignatura no existe.")

def dar_baja_estudiante(asignatura, estudiante):
    if asignatura in asignaturas:
        if estudiante in asignaturas[asignatura]:
            asignaturas[asignatura].remove(estudiante)
           
        else:
            print(estudiante+ "no está matriculado en" + asignatura)
    else:
        print("La asignatura no existe.")


while True:
    print("Menú de opciones:")
    print("1. Listar estudiantes en una asignatura")
    print("2. Matricular un estudiante en una asignatura")
    print("3. Dar de baja un estudiante de una asignatura")
    print("4. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        listar_estudiantes(input("Ingrese el nombre de la asignatura: "))
    elif opcion == "2":
        matricular_estudiante(input("Ingrese el nombre de la asignatura: "),input("Ingrese el nombre del estudiante: "))
    elif opcion == "3":
        dar_baja_estudiante(input("Ingrese el nombre de la asignatura: "),input("Ingrese el nombre del estudiante: "))
    elif opcion == "4":
        print("Saliendo del programa.")
        break
    else:
        print("Opción no válida.")