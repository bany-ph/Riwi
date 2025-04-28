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
 (NOT FINISH) --- 
'''
grades:list


def grade_by_grade():
    for i in range(len(grades)):
        grades[i] = verify_inputs(grades[i])

def verifyInt(n, restart):
    try:
        return int(n)
    except ValueError:
        print("El valor no es válido. Tiene que ser un número entero.")
        input("Presiona Enter para Continuar...\n")
        restart()

def verify_inputs(grade):
    
    while True:
        try: # in case the input is a letter/word 
            grade = int(grade)
            if (grade >= 0 and grade <= 100):
                return grade
            grade = input("Error: la nota no puede ser menor a 0 y mayor a 100 \n >")
        except ValueError:
          print("\n","==" * 10 , " ERROR" , "==" * 10)
          new_grade = input(f"Error: Cambiar '{grade}' por un numero. \nTienes que ingresar un numero: ")
          grade = new_grade #change de wrong input to the new one
          print("\n ")


def avarage ():
    global grades
    sum = 0
    for grade in grades:
        sum+=grade
    return sum / len(grades)


def input_grades():
    global grades
    grades = input("Ingrese las notas separas por comas: ").split(",")
    


        
def choose():
    print(f"\nYour grades: {grades}\n")
    c = verifyInt(input("QUE QUIERES HACER: \n1.promedio \n2.calificaciones mayores \n3.contar calificaciones\n4.volver\n > "), choose)
    
    match c:
        case 1: 
            print(f"\n{"\033[93mREPROBADO" if avarage() < 50 else "\033[32mAPROBADO" }" , end=f":\033[0m {avarage():.1f} \n")
            choose()
        case 2: 
            print("b2")
            choose()
        case 3: 
            print("b3")
            choose()
        case 4: 
            main()
        case _: 
            print("\nError: no existe\n") 
            choose()



def main():
    print("="*10, "INICIO", "="*10 )
    keep_going = input("Quieres seguir? (si/no): ")
    if keep_going.lower() == "si"  or keep_going.lower() == "s":
        input_grades()
        grade_by_grade()
        choose()
    else:
        return


main()
