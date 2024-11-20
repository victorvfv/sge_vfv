#importo datetime para el manejo de las fechas limite e inicio el diccionario de tareas
from datetime import datetime
listaTareas={}

#Este metodo hace las veces del constructor de tareas
def tareas(name,num,fecha,fin) :
    nombre=name
    prioridad=int(num)
    FechaLim=fecha
    Finalizada=fin
    return [nombre ,prioridad, FechaLim ,Finalizada ]

#Añade una tarea aal diccionario de tareas la cual tendra como clave 
#el nombre de la tarea y el valor sera toda la informacion de la tarea
def añadirTarea(nombre,num,fecha,fin):
    listaTareas[nombre]=tareas(nombre,num,fecha,fin)

# Imprime todas las tareas almacenadas en listaTareas.
# Utiliza la función "darFormato" para mostrar las tareas con un formato legible.
def PrintTareas():
    for key in listaTareas:
        tarea = getTarea(key)
        
        salida= darFormato(tarea[0],tarea[1] ,tarea[2],tarea[3])
        print(salida)
        print("")

# Devuelve una cadena formateada que representa una tarea.
# La salida incluye el nombre, prioridad, fecha límite y el estado de finalización.
def darFormato(nombre,num,fecha,fin):
    si="No"
    if(fin):
        si="Si"

    salida="Tarea: " + nombre + " su prioridad es " + str(num) + " su fecha limite es: " + str(fecha) + ", Has completado la tarea: " + si
        
    return salida

# Devuelve la tarea asociada al nombre proporcionado.
# Si la tarea no existe, retorna None.
def getTarea(nombre):
    return listaTareas.get(nombre,None)

# Guarda todas las tareas almacenadas en listaTareas en un archivo CSV.
# Cada línea del archivo representa una tarea con sus atributos separados por comas.     
def GuardarTareas():
    lineas=[]
    for key in listaTareas:
        tarea = getTarea(key)
        lineas.append(tarea[0] + "," + str(tarea[1]) + "," + str(tarea[2]) + "," + str(tarea[3])+",\n")
    with open("tareas.csv","w") as fichero:
            fichero.writelines(lineas)

# Elimina la tarea asociada al nombre proporcionado de listaTareas.
# Si la tarea no existe, no realiza ninguna acción.
def eliminarTarea(nom):
    listaTareas.pop(nom,None)

# Marca como completada la tarea asociada al nombre proporcionado.
# Actualiza el atributo "fin" de la tarea a True.
def tareaFinalizada(nom):
    tarea=getTarea(nom)
    listaTareas[nom]=tareas(tarea[0],tarea[1],tarea[2],True)

##inicio de ejecucion del codigo



# Verifica si el archivo "tareas.csv" existe; si no, lo crea vacío.
try:
    with open("tareas.csv", "x") as archivo:
        archivo.write("")
except FileExistsError:
    print("")

# Recupera las tareas almacenadas en "tareas.csv" y las carga en listaTareas.
# Cada línea del archivo se convierte en una tarea usando "añadirTarea".
try:
    with open("tareas.csv","r") as fichero:
        for linea in fichero:
            if(linea!="\n"):
                datos=linea.split(",")
                fecha = datetime.strptime(datos[2], "%Y-%m-%d").date()
                añadirTarea(datos[0],datos[1],fecha,(datos[3]=="True"))
except IndexError:
    print()

        
# Ciclo principal del programa que permite al usuario realizar diferentes acciones.
# Las opciones incluyen: añadir, listar, buscar, eliminar o marcar como completada una tarea.
while (True):

    print("Que quieres hacer?")
    print("pulsa 1 si quieres añadir una tarea")
    print("Pulsa 2 si quieres listar todas las tareas")
    print("Pulsa 3 si quieres ver una tarea especifica")
    print("Pulsa 4 si quieres eliminar una tarea especifica")
    print("Pulsa 5 si as finalizado una tarea especifica")
    print("Pulsa 0 si quieres salir")

    evento=input()

    match evento:

        case "1":
            nom=input("Di el nombre de la tarea ")
            b=True
            while(b):
                try:
                    prioridad=int(input("Di la prioridad de la tarea "))
                    b=False
                except ValueError:
                    print("Error: Debes introducir un número válido.")
            b=True
            while(b):
                try:
                    fechaInput=input("Di la fecha limie de la tarea (formato AAAA-MM-DD): ")
                    fecha = datetime.strptime(fechaInput, "%Y-%m-%d").date()
                    print("Fecha ingresada correctamente:", fecha)
                    b=False
                except ValueError:
                    print("Formato de fecha inválido.")
            añadirTarea(nom,prioridad,fecha,False)

        case "2":
            PrintTareas()

        case "3":
            tarea=getTarea(input("Di el nombre de la tarea "))
            if(tarea!=None):
                salida= darFormato(tarea[0],tarea[1] ,tarea[2],tarea[3])
            else:
                salida="Tarea inexistente"
            print(salida)

        case "4":
            salida=eliminarTarea(input("Di el nombre de la tarea "))
            if (salida==None):
                print("tarea inexistente")

        case "5":
            tareaFinalizada(input("Di el nombre de la tarea "))

        case "0":
            GuardarTareas()
            break
        case _:
            print("Input no valido ")