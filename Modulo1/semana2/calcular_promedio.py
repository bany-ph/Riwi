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




def grade_by_grade():
    for i in range(len(grades)):
        grades[i] = verify_inputs(grades[i])

def verifyInt(n, restart):
    try:
        return int(n)
    except ValueError:
        print(f"{colors.FAIL}El valor no es válido. Tiene que ser un número entero.{colors.ENDC}")
        input("Presiona Enter para Continuar...\n")
        restart()

def verify_inputs(grade):
    
    while True:
        try: # in case the input is a letter/word 
            grade = int(grade)

            if (grade >= 0 and grade <= 100):
                return grade
            
            grade = input(f"{colors.FAIL}Error: la nota no puede ser menor a 0 y mayor a 100 {colors.ENDC}\n Cambia la nota '{grade}' >")

        except ValueError:
          new_grade = input(f"Error: Cambiar '{grade}' por un numero.{colors.ENDC} \nTienes que ingresar un numero: ")
          grade = new_grade #change de wrong input to the new one
          print("\n ")


def avarage (): #promedio 
    global grades
    sum = 0
    for grade in grades:
        sum+=grade
    return sum / len(grades)


def highest_grades():
    grade_check = int(input(f" Mostrar Las notas màs grandes que: "))
    for grade in grades:
        if(not grade >= grade_check):
            continue
        print(colors.OKBLUE + ":" , grade)

def count_grade(): #contar cuántas veces aparece una nota especìfica
 while True:   
    try:
        grade = int(input(f" Nota que quieres ver cuantas veces se repite: "))
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
    c = verifyInt(c , choose)
    
    match c:
        case 1: 
            print(f"\n{colors.HEADER}PROMEDIO{colors.ENDC}\n")
            print((colors.OKGREEN + "APROBADO" if avarage() > 50 else colors.FAIL + "REPROBADO: " )+ colors.ENDC ,avarage())
            choose()
        case 2: 
             print(f"\n{colors.HEADER}NOTAS MAYORES{colors.ENDC}\n")
             highest_grades()
             choose()
        case 3: 
            print(f"\n{colors.HEADER}CONTADOR{colors.ENDC}\n")
            print(f"La nota se encuentra: {colors.OKBLUE}{count_grade()}{colors.ENDC} veces")
            choose()
        case 4: 
            main()
        case _: 
            print("\nError: no existe\n") 
            choose()



def main():
    print(f"\n  {colors.HEADER} INICIO {colors.ENDC} \n" )
    keep_going = input("Quieres seguir? (si/no): ").strip()
    if keep_going.lower() == "si"  or keep_going.lower() == "s":
        input_grades()
        grade_by_grade()
        choose()
    else:
        return


main()
