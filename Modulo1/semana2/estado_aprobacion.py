grade = None


def input_validation (message):
 while True:
    value = int(input(message))
    try:
      if value <= 100 and value >= 0:
        return value #while loop stops
      print(" Error: The grade have to be in the range of 0 to 100")
    except ValueError:
      print("Wrong input: try again")                   
      
grade = input_validation("Ingrese nota: ")

def pass_fail():
    global grade
    if(grade >= 50  ):
      print("You pass")
    else:
      print("You fail")

pass_fail()   

   