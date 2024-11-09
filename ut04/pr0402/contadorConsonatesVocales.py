def contadorVocalesYConsonates(param1):
    v=param1.count("a")
    v+=param1.count("e")
    v+=param1.count("i")
    v+=param1.count("o")
    v+=param1.count("u")
    
    c=len(param1.replace(" ",""))
    c=c-v
    print("Hay "+ str(c) +" consonantes y hay " + str(v) + " Vocales") 
n=contadorVocalesYConsonates("hola hola")
