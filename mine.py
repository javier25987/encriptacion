from tqdm import tqdm
import os

os.system('cls')

letras_minusculas = ' abcdefghijklmnñopqrstuvwxyz'
letras_mayusculas = 'ABCDEFGHIJKLMNÑOPQRSTUVWXYZ'
numeros = '0123456789'
simbolos = '''`~!@#$%^&*()-=_+{}[]:;'"<>?,./¿«»''' 

todo = letras_minusculas + simbolos + letras_mayusculas + numeros

def cifrado_cesar(simbolo, clave=3):
    global todo 
    
    posicion = todo.find(simbolo)
    posicion += clave
    posicion %= len(todo)
        
    return todo[posicion]

def xor(a, b):
    a = int(a)
    b = int(b)
    k = (a and (not b)) or (b and (not(a)))
    
    return str(int(k))

c_d = 1

print('desea cifrar o descifrar?\n    1. cifrar\n    2. descifrar')

while True:
    try:
        v_d_v = int(input('> __ : '))
        if v_d_v in [1, 2]:
            c_d = 1 if v_d_v == 1 else -1
            break
        else:
            print('el valor introducido no representa una opcion')
    except:
        print('el valor introducido no representa una opcion')

print()
print('por favor introduzca el nombre de un archivo de texto\nque se encuentre en el repositorio de el scrip\nno incluya la terminacion .txt')
print()

while True:
    try:
        archivo = input('> archivo a abrir: ') + '.txt'

        with open(archivo, 'r') as f:
            contenido_archivo = f.readlines()
            
        break
    except:
        print(f'el archivo no se encuentra en el repositorio')
    
new_contenido = ''

print()
while True:
    try:
        clave_c = int(input('> clave de (des)cifrado: '))
        clave_c = bin(clave_c)[2:]
        break
    except:
        print('la clave tiene que ser un valor numerico entero')
        
def generador_random():
    global clave_c
    
    k = clave_c
    n = xor(k[0], k[1])
    k = k[1:] + n
    clave_c = k

print()
for i in tqdm(contenido_archivo):
    renglon = i
    renglon = renglon.rstrip()
    temporal_renglon = ''
    
    for j in renglon:
        temporal_renglon += cifrado_cesar(j, clave=int(clave_c, 2)*c_d)
        generador_random()
        
    temporal_renglon += '\n'
    new_contenido += temporal_renglon
    
print()
print('que desea hacer con el texto obtenido?\n    1. escribir en el archivo\n    2. mostrar en consola')

while True:
    try:
        v_d_a = int(input('> __ : '))
        if v_d_a in [1, 2]:
            break
        else:
            print('el valor introducido no representa una opcion')
    except:
        print('el valor introducido no representa una opcion')

match v_d_a:
    case 1:
        with open(archivo, 'w') as f:
            f.write(new_contenido)
        print()
        input('el archivo ha sido (des)cifrado,\npresione enter para terminar...')
    case 2:
        print()
        print(new_contenido)
        
        while True:
            confi = input('quieres escribir en el archivo [s/n]?')
            
            if confi in ['s', 'n']:
                break
            else:
                print('la respuesta no esta entre las opciones')
        
        if confi == 's':
            with open(archivo, 'w') as f:
                f.write(new_contenido)
            print()
            input('el archivo ha sido (des)cifrado,\npresione enter para terminar...')
        else:
            input('tarea terminada, presione enter para terminar...')
    case _:
        print()
        print('si quiera como hiciste eso?')
        
        

    
    
    


