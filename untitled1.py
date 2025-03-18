path=r"C:\Users\Rain City\Desktop\restaurant management\book3.csv"
import pandas as pd
data=pd.read_csv(path,encoding='Utf-8-sig')

import random
class Restaurant:
    def __init__(self):
        self.menu={}
        self.menu=data
        self.oorders= {}
        self.tables={
            '1':[1],
            '2':[1],
            '3':[1],
            '4':[],
            '5':[1]
            }
    def add_item_to_menu(self, item, price): 
        self.menu[item.upper()] = price 
        data=pd.DataFrame(self.menu)
        data.to_csv(path,index=False,encoding='Utf-8-sig')
        print(f"Item '{item}' ba gheymat {price} be menu ezafe shod") 
    def remove_item_from_menu(self, item): 
        if item in self.menu: 
            del self.menu[item] 
            data=pd.DataFrame(self.menu)
            data.to_csv(path,index=False,encoding='Utf-8-sig')
            print(f"Item '{item}' az menu bardashte shod") 
        else: 
            print(f"Item '{item}' yaft nashod") 
    def update_item_price(self, item, price): 
        if item in self.menu: 
            self.menu[item] = price 
            data=pd.DataFrame(self.menu)
            data.to_csv(path,index=False,encoding='Utf-8-sig')
            print(f"gheymate '{item}' be in mablagh {price} taghir kard") 
        else: 
            print(f"Item '{item}' yaft nashod") 
    def show_menu(self): 
          if len(self.menu.keys())==0: 
                print("menu khalie")
          else: 
                print("Menu:") 
                for item, price in self.menu.items(): 
                    print(item,":",[str(price)][0][5:11])
                    
    def table(self):
                flag=False
                    
                for i in range(1,6):
                    if len(self.tables[str(i)])==0:
                        self.tables[str(i)].append(i)
                        print(f"miz to'{i}' ast")
                        flag=True
                        break               
                
                 
                return flag ,i    
            
                        
                        
                
    
    def place_order(self, item,miz): 
            if item in self.menu:
                self.tables[str(miz)].append([item.upper(),self.menu[str(item)]]) 
                print(f"Item '{item}' dar miz '{miz}' ordered.")                       
            else: 
                print(f"Item '{item}' yaft nashod") 
    def code_online(self):
            y= random.randrange(10000,50000)
            while str(y)==self.oorders.keys():
                y= random.randrange(10000,50000)
            return y
   
    
    def online_order(self, item,key): 
            if item in self.menu:               
                
                if str(key) in self.oorders.keys():
                    self.oorders[str(key)].append([item.upper(),self.menu[str(item)]])
                else:
                    self.oorders.update({str(key):[[item.upper(),self.menu[str(item)]]]}) 
                print(self.oorders[str(key)])
                print(f"Item '{item}' ba code : '{key}' sefaresh dade shod")
                
               
                
            else: 
                print(f"Item '{item}' yaft nashod") 
    def show_orders(self , miz):
            if len(self.tables[str(miz)])==0:
                print("hanoz sefaresh nadady") 
            else:
                print("Orders:",self.tables[str(miz)]) 
                 
                   
    def calculate_bill(self,miz): 
            total=0
            for i in range (len(self.tables[str(miz)])-1):
                total=total+self.tables[str(miz)][i+1][1]
            print(total)
            print("alan pardakht mikony?")
            z=int(input("1.yes / 2.no ---->"))
            if z==1:
                print("pardakht shod")
                del self.tables[str(miz)]
                print(" khosh amadid")
                return
            if z==2:
                return
            
    def calculate_online(self,key,A,PH): 
            total=0
            for i in range (len(self.oorders[str(key)])):
                total=total+self.oorders[str(key)][i][1]
            print(total)
            print("alan pardakht mikony?")
            z=int(input("1.yes / 2.no ---->"))
            if z==1:
                print("pardakht shod")
                print(f" sefaresh shoma be in address: '{A}' va  in shomare tamas:'{PH}' ta 30min dige ersal mishavad ")
                return
            if z==2:
                return
                
        
        
        
def main():
            restaurant = Restaurant() 
            while True:
                print("\n1. Admin")
                print("2. Customer")
                print("3. Exit") 
                choice = input("koodom : ")
                if choice == "1":
                    print("\nAdmin Menu:")
                    print("1. ezefe kardan item")
                    print("2. hazf item az menu") 
                    print("3. Update gheymate item")
                    print("4. Show menu")
                    admin_choice = input("koodom yeki : ") 
                    if admin_choice == "1":
                        item = input("Enter item name: ") 
                        price = float(input("Enter item price: ")) 
                        restaurant.add_item_to_menu(item, price)
                    elif admin_choice == "2": 
                        item = input("esm itemo vared kon")
                        restaurant.remove_item_from_menu(item)
                    elif admin_choice == "3":
                        item = input("esm itemo vared kon ")
                        price = float(input("gheymat jadido vared kon "))
                        restaurant.update_item_price(item, price)
                    elif admin_choice == "4": 
                        restaurant.show_menu() 
                    else:
                        print("out of range")
                elif choice == "2":
                 while True:
                    
                    print("\nCustomer Menu:")
                    print("1. Show menu")
                    print("2. sefaresh ") 
                    print("3. Show orders") 
                    print("4. Calculate bill") 
                    customer_choice = input("koodom : ")
                    
                    
                    if customer_choice == "1":                     
                        restaurant.show_menu()                       
                        tsm =int(input("sefaresh midi? (1.yes/2.no) ------> "))
                        if tsm==2:
                            continue
                        
                        elif tsm==1:
                            x,miz=restaurant.table()
                            if x==False :
                                print("resturant fulle")
                                
                                
                            else:
                                while True:
                                    item =input("sefaresh bede ")
                                    restaurant.place_order(item.upper(),miz)
                                    n=int(input("EDAME MIDY? ---> 1.yes / 2.no ----> "))
                                    if n==2:
                                       restaurant.show_orders(miz) 
                                       break
                                    elif n==1:
                                       True
                            
                        else:
                            print("\n")
                            print("out of range")
                            break
                        
                    elif customer_choice == "2": 
                        print("1. online ")
                        print("2. hozoory ")
                        tarighe = input("kodom?--->")
                        if tarighe=="1":
                            key=restaurant.code_online()
                            adres=input("enter your addres ----> ")
                            phone_number=input("phone number ---->")
                            while True:
                                item =input("Enter item name: ")
                                restaurant.online_order(item.upper(),key)
                                n=int(input("EdAME MIDY? ---> 1.yes / 2.no ----> "))
                                if n==2:
                                   restaurant.calculate_online(key,adres,phone_number)
                                   break
                                elif n==1:
                                   True
                            
                           
                            
                        elif tarighe=="2":
                            print("1. mikhori ")
                            print("2. mibari ")
                            natije=input("--->")
                            if natije=="1":
                                x,miz=restaurant.table()
                                
                               
                                if x==False :
                                    print("resturant fulle")
                                    break
                                    
                                    
                                else:
                                        restaurant.show_menu()
                                        while True:
                                            item =input("Enter item name: ")
                                            restaurant.place_order(item.upper(),miz)
                                            n=int(input("EDAME MIDY? ---> 1.yes / 2.no ----> "))
                                            if n==2:
                                               restaurant.show_orders(miz) 
                                               break
                                            elif n==1:
                                               True
                            if natije=="2":
                                restaurant.show_menu()
                                key=restaurant.code_online()
                                adress=input("enter your addres ----> ")
                                phone_number=input("phone number ---->")
                                while True:
                                    item =input("SEFARESH BEDE")
                                    restaurant.online_order(item.upper(),key)
                                    n=int(input("EdAME MIDY? ---> 1.yes / 2.no ----> "))
                                    if n==2:
                                       restaurant.calculate_online(key , adress , phone_number)
                                       break
                                    elif n==1:
                                       True
                                
                                break
                 
                    elif customer_choice == "4": 
                            restaurant.calculate_bill(miz) 
                            continue
                    else: 
                            print("Invalid choice.")
                elif choice == "3":
                    print("Exiting program.")
                    break
                else: 
                    print("Invalid choice.")
                    return miz    
if __name__ == "__main__":
            main()
