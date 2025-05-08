#week 3: 


class colors: #colors for console
   HEADER = '\033[95m \t' #\t: to make the text 'center'
   GREEN  = '\033[32m' 
   BLUE   = '\033[94m'
   FAIL   = '\033[91m' #Errors
   ENDS   = '\033[0m' #end the color

products = {}
input_key:str # help to keep the request for: delete_product(), add_product()...etc


"""check if a product exist in products"""
def product_exist(key):
    #check if the product requested exist
    for product in products.keys():
        if product == key:
            return True
       
    return False
    
    

def add_product():
    global input_key
    """ 

        check if the inputs are correct
        check if the products already exist
        add the product
    
    """
    try:
        input_key = input(colors.BLUE +"Insert the name of the product you wanna add: "+ colors.ENDS).strip().lower() # -> read new key, delete all the spaces and convert all the word in lowerCase
        if not product_exist(input_key):
            new_price = float(input(f"{colors.BLUE}Insert the price of the product: {colors.ENDS} ").strip())
            new_amount = float(input(f"{colors.BLUE}Insert the amount of the product: {colors.ENDS} ").strip())
            products[input_key] = (new_price,new_amount)
            print(f"{colors.GREEN} '{input_key}' added succesfully")
        else:
            print(f"{colors.FAIL}The product already exist")
    except ValueError:
        print(f"{colors.FAIL} Wrong inputs: Price and amount have to be numbers: try again\n")



def update_price():
    global input_key
    try:
        input_key = input(f"{colors.BLUE}Insert the name of the product you wanna changes:{colors.ENDS} ").strip().lower()
        if product_exist(input_key):
            products[input_key] = (float(input(f"{colors.BLUE}Insert the new price:{colors.ENDS} ")), products[input_key][1]) #change the price and keep the amount
            print(f"{colors.GREEN} '{input_key}' price succesfully changed")
        else:
            print(f"{colors.FAIL}The product doesn't exist")      
    except ValueError:
        print(f"{colors.FAIL} Error: The price have to be a number")

        

def delete_product():
    global input_key
    input_key = input("Insert the product you wanna delete: ").lower().strip()
    try:
       products.pop(input_key)
       print(f"{colors.GREEN}The product '{input_key}' was delete succesfully")
    except:
        print(f"{colors.FAIL}The product '{input_key}' doesn't exist")
    






"""show_product() show all the elements in products

    show_one_product() show the produdct requested
"""
def show_products():
    """Show all the products"""
    for key,value in products.items():
        print(f"{colors.GREEN}{key} -> price: {value[0]} || amount: {value[1]}")

def show_one_product():
    global input_key
    try:
        input_key = input("Insert the product you wanna see: ").lower().strip()
        print(f"{colors.GREEN}{input_key}-> price: {products[input_key][0]} || amount: {products[input_key][1]}")
    except:
        print(f"{colors.FAIL}Error: the '{input_key}' doesn't exist")


def total_invetory():
    total = sum(map(lambda x: x[0] * x[1], products.values()))
    show_products()
    print(f"\nTotal: {total}")





def show_menu():
    print(colors.HEADER + "MENU" + colors.ENDS)
    print(f"{colors.BLUE}1.{colors.ENDS}Add product") 
    print(f"{colors.BLUE}2.{colors.ENDS}Show products")
    print(f"{colors.BLUE}3.{colors.ENDS}Search one product")
    print(f"{colors.BLUE}4.{colors.ENDS}Delete product") 
    print(f"{colors.BLUE}5.{colors.ENDS}Update price") 
    print(f"{colors.BLUE}6.{colors.ENDS}Total Inventory")
    print(f"{colors.BLUE}7.{colors.ENDS}Exit")



"""menu"""
def main():
    print("\n")
    show_menu()
    des = input("> ").strip()
    match des:
        case "1":
            print(f"{colors.HEADER}ADD PRODUCT{colors.ENDS}")
            add_product()
            main()
        case "2":
            print(f"{colors.HEADER}ALL PRODUCTS{colors.ENDS}")
            show_products()
            main()
        case "3":
            print(f"{colors.HEADER}PRODUCT REQUEST{colors.ENDS}")
            show_one_product()
            main()
        case "4":
             print(f"{colors.HEADER}DELETE PRODUCT{colors.ENDS}")
             delete_product()
             main()
        case "5":
            print(f"{colors.HEADER}UPDATE PRODUCT PRICE{colors.ENDS}")
            update_price()
            main()
        case "6":
            print(f"{colors.HEADER}INVENTORY TOTAL{colors.ENDS}")
            total_invetory()
            main()
            
        case "7":
            print(f"{colors.GREEN}Byeee")
            return #main() close and end the proccess
        case _ :
            print(f"{colors.FAIL}Wrong input")
            main()




main() #start
