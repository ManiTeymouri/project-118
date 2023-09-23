DATABASE = "database.txt"

class account:

    DATABASE_DICT = {
            "location_status":"",
            "Name":"",
            "Phone":"",
            "Address":"",
    }

    # این متد کمک میکنه تا من به دیتا های داخل دیتابیس دسترسی پیدا کنم و اونارو تبدیل به دیکشنری کنم
    def __Convert_DATA():
        file = open(DATABASE,"r")
        lines = file.readlines()
        file.close()
        List_Lines = dict()
        # lines to dict
        for  i in range(len(lines)):
            List_Lines[f"{i}"] = lines[i]
        # convert all value in lines to dict
        for key,value in List_Lines.items():
            value = eval(value)
            List_Lines[key] = value
        return List_Lines




    def create(location_status: int, Name: str,Phone: str,Address: str):
        # information of account 
        account.DATABASE_DICT["location_status"] = location_status.lower()
        account.DATABASE_DICT["Name"] = Name.lower()
        account.DATABASE_DICT["Phone"] = Phone.lower()
        account.DATABASE_DICT["Address"] = Address.lower()

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

    def search(location_status,data):
        mydict = account.__Convert_DATA()
        Pointer = 0
        for key,value in mydict.items():
                    if location_status in value["location_status"] and data in value["Name"]:
                        print(f"==================={value['Name']}===================")
                        for lil_key,lil_value in value.items():
                            print(f"{lil_key} : {lil_value}")
                        print(f"=====================================================")
                    elif location_status in value["location_status"] and data in value["Phone"]:
                        print(f"==================={value['Name']}===================")
                        for lil_key,lil_value in value.items():
                            print(f"{lil_key} : {lil_value}")
                        print(f"=====================================================")
                        Pointer += 1
                    elif location_status in value["location_status"] and data in value["Address"]:
                        print(f"==================={value['Name']}===================")
                        for lil_key,lil_value in value.items():
                            print(f"{lil_key} : {lil_value}")
                        print(f"=====================================================")
        if Pointer == 0:
            print("Account not Exist")

             
                            

    
        


print("Welcome to Oprator 118 Account")
print("-------------------------------")

while True:
    print("-------------------------------")
    print("1.search Accounts\n2.create Account\n3.edit Account\n4.delete Account\n5.exit")
    print("-------------------------------")
    try:
        option = int(input("Enter Your Option:"))
        print("-------------------------------")
        match option:
            case 1:
                while True:
                    print("-------------------")
                    print("please choose location status you want search.")
                    print("1.Residental\n2.Office\n3.Markets\n4.all types")
                    print("-------------------")
                    location_status = int(input(""))
                    print("-------------------")
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
                        case 4:
                            location_status = ""
                            break
                        case value:
                            print("please choose between options.")
                print("--------------------------------------------")
                print("you can search by Phone/Name/Address : ")
                search = input("search :>")
                print("--------------------------------------------")
                account.search(location_status.lower(),search.lower())
                print("--------------------------------------------")
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

    