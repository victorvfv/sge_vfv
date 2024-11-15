import tarea

listaTareas=[]

def añadirTarea():
    listaTareas.append(tarea.tareas(input("Di el nombre de la tarea "),12,"ayer",True))

def PrintTareas():
    for lista in listaTareas:
        si="No"
        if(lista[3]):
            si="Si"
        salida="Tarea: " + lista[0] + " su prioridad es " + str(lista[1]) + " su fecha limite es: " + lista[2] + ", Has completado la tarea: " + si
        print(salida)
        
            


while (True):
    print("Que quieres hacer?")
    print("pulsa 1 si quieres añadir una tarea")
    print("Pulsa 2 si quieres listar todas las tareas")
    print("Pulsa 0 si quieres salir")

    evento=input()

    match evento:
        case "1":
            añadirTarea()
        case "2":
            PrintTareas()
        case "0":
            break
