'''
Calcular el promedio:
    Permitir al usuario ingresar una lista de calificaciones (separadas por comas)
    Calcular y mostrar el promedio de las calificaciones en la lista
Contar calificaciones mayores:
    Preguntar al usuario por un valor específico
    Contar cuántas calificaciones en la lista son mayores que este valor
Verificar y contar calificaciones específicas:
    Permitir al usuario ingresar una lista de calificaciones (separadas por comas)
    Calcular y mostrar el promedio de las calificaciones en la lista
 ()
'''
grades:list

class colors: # para cambiar color de texto de la consola
    HEADER = '\033[95m' #titulos/
    OKBLUE = '\033[94m' 
    OKGREEN = '\033[32m' #Para 'aprobado' principalmente
    FAIL = '\033[91m' #para errores con el input
    WARNING = '\033[93m' #aviso
    ENDC = '\033[0m' #cerrar el color



def verify_int(n, restart):
    try:
        return int(n) #string -> int
    except ValueError: #si n no es un numero
        print(f"{colors.FAIL}El valor no es válido. Tiene que ser un número entero.{colors.ENDC}")
        input("Presiona Enter para Continuar...\n")
        restart()

def verify_inputs():
    global grades
    i:int = 0 #para la lista
    while True:
        try: # in case the input is a letter/word 
            grades[i] = int(grades[i])

            if (grades[i] >= 0 and grades[i] <= 100):
                i+=1
                if i == len(grades) :
                    break
                continue
            

            grades[i] = input(f"{colors.FAIL}Error: la nota no puede ser menor a 0 o mayor a 100 {colors.ENDC}\n Cambia la nota '{grades[i]}' >")

        except ValueError:
          grades[i] = input(f"{colors.FAIL}Error: Cambiar '{grades[i]}' por un numero.{colors.ENDC} \nTienes que ingresar un numero: ")
      
          print("\n ")


def average (): #promedio 
    global grades
    total:int = 0
    for grade in grades:
        total += grade
    return total / len(grades)


def highest_grades(): #muestra las notas más altas de x numero
    grade_check = int(input(" Mostrar Las notas màs grandes que: "))
    for grade in grades:
        if( grade < grade_check):
            continue
        print(colors.OKBLUE + ":" , grade)

def count_grade(): #contar cuántas veces aparece una nota especìfica
 while True:   
    try:
        grade = int(input(" Nota que quieres ver cuantas veces se repite: "))
        return grades.count(grade)
    except ValueError:
        print(f"{colors.FAIL}ERROR: El valor que ingresaste no se encuentra en la lista o el valor no es un numero {colors.ENDC}" )
        
     

def input_grades():
    global grades
    while(True): #se repite hasta que el usuario coloque bien el input de las notas
        grades = input(f"Ingrese las notas separas por comas ({colors.WARNING}Solo Numericos{colors.ENDC}): ").replace(" ","") #lee y quita todos lo espacios innecesarios en el input
        if(',' in grades):
            grades = grades.split(",") #separa la cadena en una lista
            break;
        else:
            print(f"{colors.FAIL}ERROR:{colors.ENDC} {colors.WARNING}Tienes que ingresar las notas separadas por comas (ej: 100,50,30,100...){colors.ENDC} \n")
    


        
def choose():
    print(f"\n{colors.OKBLUE}Your grades: {grades}{colors.ENDC}\n")
    c = input(f"{colors.HEADER}QUE QUIERES HACER:{colors.ENDC} \n1.promedio \n2.calificaciones mayores \n3.contar cuántas veces aparece una nota especìfica\n4.volver\n > ")
    c = verify_int(c , choose) #verifica que el input sea el adecuado
    
    match c: #promedio
        case 1: 
            print(f"\n{colors.HEADER}PROMEDIO{colors.ENDC}\n")
            print((colors.OKGREEN + "APROBADO" if average() > 50 else colors.FAIL + "REPROBADO: " )+ colors.ENDC ,average())
            choose()
        case 2: # calificacines mayores
             print(f"\n{colors.HEADER}NOTAS MAYORES{colors.ENDC}\n")
             highest_grades()
             choose()
        case 3: # Notas repetidas en la lista
            print(f"\n{colors.HEADER}CONTADOR{colors.ENDC}\n")
            print(f"La nota se encuentra: {colors.OKBLUE}{count_grade()}{colors.ENDC} veces")
            choose()
        case 4: #volver al inicio
            main()
        case _: 
            print(f"{colors.FAIL}\nError: no existe\n{colors.ENDC}") 
            choose()



def main():
    print(f"\n  {colors.HEADER} INICIO {colors.ENDC} \n" )
    keep_going = input("Quieres seguir? (si/no): ").strip()
    if keep_going.lower() == "si"  or keep_going.lower() == "s":
        input_grades() #para ingresar las notas
        verify_inputs()#verificar que las notas esten correctas (numericos y en  el rango de 0-100)
        choose() #menu de opciones
    else:
        return #salir del programa


main()
