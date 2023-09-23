PhoneBASE = "Phonebase.txt"

class account:
    # این متد خط های خالی رو داخل دیتا بیس پاک میکنه
    def __remove_empty_lines():
            with open(PhoneBASE, 'r') as file:
                lines = [line for line in file if line.strip()]
            with open(PhoneBASE, 'w') as file:
                file.writelines(lines)
    __remove_empty_lines()
    PhoneBASE_DICT = {
            "location_status":"",
            "Name":"",
            "Phone":"",
            "Address":"",
    }

    # این متد کمک میکنه تا من به دیتا های داخل دیتابیس دسترسی پیدا کنم و اونارو تبدیل به دیکشنری کنم
    def __Convert_DATA():
        with open(PhoneBASE,"r") as file:
            lines = file.readlines()
        List_Lines = dict()
        # lines to dict
        for  i in range(len(lines)):
            List_Lines[f"{i}"] = lines[i]
        # convert all value in lines to dict
        for key,value in List_Lines.items():
            value = eval(value)
            List_Lines[key] = value
        return List_Lines



    # متد ساخت اکانت 
    def create(location_status: int, Name: str,Phone: str,Address: str):
        # information of account 
        account.PhoneBASE_DICT["location_status"] = location_status.lower()
        account.PhoneBASE_DICT["Name"] = Name.lower()
        account.PhoneBASE_DICT["Phone"] = Phone.lower()
        account.PhoneBASE_DICT["Address"] = Address.lower()

        # check if phone exist don't be added
        file = open(PhoneBASE,"r")
        PhoneBASE_LINES = file.readlines()
        file.close()
        Pointer = 0
        for i in range(len(PhoneBASE_LINES)):
            if Phone in PhoneBASE_LINES[i]:
                Pointer += 1
       
        # add Number 
        if Pointer == 0:
            file = open(PhoneBASE,"a")
            file.write(f"{str(account.PhoneBASE_DICT)}\n")
            file.close()
            print("------------------------")
            print(f"{Phone} added .")
            print("------------------------")
        else:
            print("------------------------")
            print(f"{Phone} Number Exists")
            print("------------------------")
        account.__remove_empty_lines()

    #متد سرچ کردن  
    def search(location_status,Phone):

        mydict = account.__Convert_DATA()
        Pointer = 0
        for key,value in mydict.items():
                    if location_status in value["location_status"] and Phone in value["Name"]:
                        print(f"==================={value['Name']}===================")
                        for lil_key,lil_value in value.items():
                            print(f"{lil_key} : {lil_value}")
                        Pointer += 1
                        print(f"=====================================================")
                    elif location_status in value["location_status"] and Phone in value["Phone"]:
                        print(f"==================={value['Name']}===================")
                        for lil_key,lil_value in value.items():
                            print(f"{lil_key} : {lil_value}")
                        print(f"=====================================================")
                        Pointer += 1
                    elif location_status in value["location_status"] and Phone in value["Address"]:
                        print(f"==================={value['Name']}===================")
                        for lil_key,lil_value in value.items():
                            print(f"{lil_key} : {lil_value}")
                        Pointer += 1
                        print(f"=====================================================")
        if Pointer == 0:
            print("Account not Exist")
        account.__remove_empty_lines()

    def delete(location_status,Phone):
        with open(PhoneBASE,"r") as file:
            lines = file.readlines()
        Pointer = 0
        for i in range(len(lines)):
            if location_status in lines[i] and Phone in lines[i]:
                lines[i] = ""
            else:
                Pointer += 1
        if Pointer == 0:
            print("Number not exists.")
        else:
            with open(PhoneBASE,"w") as file:
                file.writelines(lines)
                print("============================")
                print(f"{Phone} deleted.")
                print("============================")
           
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
                while True:
                    try:
                        print("-------------------")
                        print("1.Residental\n2.Office\n3.Markets\n4.all types")
                        print("-------------------")
                        location_status = int(input("choose option :"))
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
                    except TypeError:
                        print("please Enter only number.")
                
                Phone = input("Enter phone number :")
                account.delete(location_status.lower(),Phone.lower())
            case 5:
                print("see you later...👋👋👋")
                exit()
            case value:
                print(f" {value} not in the option list")
                print("-------------------------------")
    except ValueError:
        print("please choose option(number only)")
        print("-------------------------------")

    