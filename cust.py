class Customer:  # encapsulation
    def __init__(self,name,gen): #__init__ is the magic method and name and gen ius variable
        self.name=name
        self.gen=gen

def greet(customer): 
    if customer.gen == "Male":
        print("Hello",customer.name,"Sir")
    else:
        print("Hello",customer.name,"Mam")

#def boss(customer):
    # if customer.name == customer.name :
    #     print("customer is valid")
    # else:
    #     print("Invalid")

cust=Customer("Sharique","Male")    #creating and object and calling it by reference
greet(cust)
#boss(cust)   #call by reference
cust1 =Customer("Farhana","female")
new_cust=greet(cust1)
#print(new_cust)
