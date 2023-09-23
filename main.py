DATABASE = "database.txt"

class account:

    DATABASE_DICT = {
            "location_status":"",
            "Name":"",
            "Phone":"",
            "Address":"",
    }

    def create(location_status: int, Name: str,Phone: str,Address: str):
        # information of account 
        account.DATABASE_DICT["location_status"] = location_status
        account.DATABASE_DICT["Name"] = Name
        account.DATABASE_DICT["Phone"] = Phone
        account.DATABASE_DICT["Address"] = Address

        # check if phone exist don't be added
        file = open(DATABASE,"r")
        DATABASE_LINES = file.readlines()
        file.close()
        Pointer = 0
        for i in range(len(DATABASE_LINES)):
            if Phone in DATABASE_LINES[i]:
                Pointer += 1
       
        # add Number 
        if Pointer == 0:
            file = open(DATABASE,"a")
            file.write(f"{str(account.DATABASE_DICT)}\n")
            file.close()
            print("------------------------")
            print(f"{Phone} added .")
            print("------------------------")
        else:
            print("------------------------")
            print(f"{Phone} Number Exists")
            print("------------------------")

    def search(data):
        Listed_Data = dict()
        file = open(DATABASE,"r")
        lines = file.readlines() # read database lines
        file.close() #  close file 
        for line in range(len(lines)): # loop in lines
            Listed_Data[f"{line}"] = lines[line] # Make New Dict for search

        for key,value in Listed_Data.items():
            value = eval(value) # Convert Text to dict format
            Listed_Data[key] = value
        Pointer = 0
        for key,value in Listed_Data.items(): # search on Dict
            if data in value["Phone"]:
                print(value)
                Pointer += 1
            elif data in value["Name"]:
                print(value)
                Pointer += 1
            elif data in value["Address"]:
                print(value)
                Pointer += 1
        if Pointer == 0:
            print("------------------------")
            print("Account Not Exist") 
            print("------------------------")



                            

    
        



print("Welcome to Oprator 118 Account")
print("-------------------------------")

while True:
    print("1.search Accounts\n2.create Account\n3.edit Account\n4.delete Account\n5.exit")
    print("-------------------------------")
    try:
        option = int(input("Enter Your Option:"))
        print("-------------------------------")
        match option:
            case 1:
                print("------------------------")
                print("You can search by Name/Phone/Address")
                search = input("Name/Phone/Address ? :")
                account.search(search)
                print("------------------------")
            case 2:

                while True:
                    try:
                        print("--------------------------")
                        print("1.Residental\n2.Office\n3.Markets\n")
                        print("--------------------------")                    
                        location_status = int(input("Enter between options :"))
                        match location_status:
                            case 1:
                                location_status = "Residental"
                                break
                            case 2:
                                location_status = "Office"
                                break
                            case 3:
                                location_status = "Markets"
                                break
                            case value:
                                print("please choose between options.")
                    except ValueError:
                        print("Please Enter a number not string")
                        print("====================================")
                        
                Name = input("Enter Name :")
                while True:
                    try:
                        Phone = input("Enter phonenumber : ")
                        if Phone[0] == "0":
                            Phone = Phone.replace(Phone[0],"")
                            int(Phone)
                        else:
                            int(Phone)
                        Phone = str(Phone)
                        Phone = "0" + Phone
                        if len(Phone) == 11:
                            break
                        else:
                            print("please enter correct number (11 digit)")
                    except ValueError:
                        print("Please Enter a number not string")
                        print("====================================")
                
                Address = input("Enter Address :")
                account.create(location_status,Name,Phone,Address)

            case 3:
                ...
            case 4:
                ...
            case 5:
                print("see you later...👋👋👋")
                exit()
            case value:
                print(f" {value} not in the option list")
                print("-------------------------------")
    except ValueError:
        print("please choose option(number only)")
        print("-------------------------------")

    