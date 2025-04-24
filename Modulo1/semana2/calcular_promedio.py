'''
Permitir al usuario ingresar una lista de calificaciones (separadas por comas)
Calcular y mostrar el promedio de las calificaciones en la lista
 (NOT FINISH)
'''

def input_validation(grade): #check if the input is alright
    global grades
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
          
         
grades = input("ingrese las notas separadas por comas: ").split(",")
for i in range(len(grades)):
   grades[i] = input_validation(grades[i]) 

print("=" * 35)
print(f"Grades: {grades}\n")
print(f"Avarage: {avarage()}")
print("=" * 35)


