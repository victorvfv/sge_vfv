import tarea

listaTareas=[]

def añadirTarea():
    listaTareas.append(tarea.tareas(input("Di el nombre de la tarea "),12,"ayer",True))

print(listaTareas)