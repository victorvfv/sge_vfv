from datetime import date

nombre=""
prioridad=""
FechaLim=""
Finalizada=""

def tareas(name,num,fecha,fin) :
    nombre=name
    prioridad=int(num)
    FechaLim=fecha
    Finalizada=fin
    return [nombre ,prioridad, FechaLim ,Finalizada ]
