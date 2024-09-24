from utilidades import leer_instrucciones, labels, is_pseudo
from ensamblador import ensamblar_instrucciones
from pseudoinstrucciones import compile_pseudo

instrucciones: list

def leer_labels(instrucciones):
    i = 0
    insts = []
    for instruccion in instrucciones.copy():
        if instruccion == "":
            continue
        if ":" in instruccion:
            labels[instruccion.replace(":", "")] = i
            i -= 1
            instrucciones.remove(instruccion)
        else:
            match, equivalencia = is_pseudo(instruccion)
            if isinstance(match, dict):
                inst = compile_pseudo(equivalencia, match, i)
                insts += inst
                if len(inst) > 1:
                    i += 1
            else:
                insts.append(instruccion)  
        i += 1
    
    return insts

def main():
    archivo_entrada = './entrada.txt'  # Archivo de entrada
    global instrucciones
    instrucciones = leer_instrucciones(archivo_entrada) #Va y lee las instrucciones del archivo de entrada
    instrucciones = leer_labels(instrucciones)
    instrucciones = [inst for inst in instrucciones if not(":" in inst or inst == "")]
    instrucciones_binarias = ensamblar_instrucciones(instrucciones) #Va y ensambla las instrucciones
    
    return instrucciones_binarias
    

instrucciones_binarias = main()

print(instrucciones_binarias)
