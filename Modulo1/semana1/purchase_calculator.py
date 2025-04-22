#Semana 1


def input_validation(message, discount=False):
   while True:
        try:
            value = int(input(message))
          
            if discount and (value < 0 or value > 100): #if the value is discount and the value is wrong then 
                input("Wrong input: discount have to be in the rage of 0 to 100")
            elif(not discount) and value <= 0: #if the value isn´t discount and value is 0 or negative then
                input("Wrong input: The input Can't be 0 or negative")
            else:
                return value #while stop
            print("- " * 20) 
        except ValueError:
            print("--Wrong input: Try again--")
   


def total(unit,amount,discount, apply_discount = False):
    if(apply_discount):
        return f"{unit * amount - ((unit * amount) * (discount / 100)):.2f}"
    else:
        return f"{unit * amount:.2f}"



product_name = input("product name: ")
unit_price = input_validation("Unit price of the product: ")
product_amount = input_validation("Amount of product: ")
discount = input_validation("Discount: ", True)

print("=" * 35)
print(f"Name                  {product_name}\n")
print(f"Unit Price            {unit_price}")
print(f"Amount                {product_amount}")
print(f"Total                 {total(unit_price,product_amount,discount)}") # print total without discount
print(f"Discount              {discount}%")
print(f"Total with discount   {total(unit_price,product_amount,discount,True)}") #print total with discount
print("=" * 35)
