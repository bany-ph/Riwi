    #Semana 1


def validation(unit, amount, discount):
    return not(unit <= 0 or amount <= 0 or discount > 100 or discount < 0)
   


def total_no_discount(unit, amount):
    return unit * amount   

def apply_discount(total, percentage_discount): #Parameters : total of the price without the discount, and the percentage of the discount. 
    if total == 0:
        return total
    else:
        return total - (total * (percentage_discount/100))


def calculate_total(unit, amount, product_discount):

    return apply_discount(total_no_discount(unit,amount), product_discount)



while True:
    try:
        product_name = input("product name: ")
        product_amount = (int(input("amount of the product: ")))
        unit_price = (float(input("unit price: ")))
        product_discount = (int(input("Product discount: ")))
        if(validation(unit_price, product_amount, product_discount)): #inputs validations 
           print(f"{product_name}  total = {calculate_total(unit_price, product_amount,product_discount):.2f}")
           break
        else:
            print("Wrong Inputs")
        
    except ValueError:
        print("Invalid input: try again")        