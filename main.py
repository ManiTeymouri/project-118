DATABASE = "database.txt"

class account:
    # این متد خط های خالی رو داخل دیتا بیس پاک میکنه
    def __remove_empty_lines():
            with open(DATABASE, 'r') as file:
                lines = [line for line in file if line.strip()]
            with open(DATABASE, 'w') as file:
                file.writelines(lines)
    __remove_empty_lines()
    DATABASE_DICT = {
            "location_status":"",
            "Name":"",
            "Phone":"",
            "Address":"",
    }

    # این متد کمک میکنه تا من به دیتا های داخل دیتابیس دسترسی پیدا کنم و اونارو تبدیل به دیکشنری کنم
    def __Convert_DATA():
        with open(DATABASE,"r") as file:
            lines = file.readlines()
        List_Lines = dict()
        # lines to dict
        for  i in range(len(lines)):
            List_Lines[i] = lines[i]
        # convert all value in lines to dict
        for key,value in List_Lines.items():
            value = eval(value)
            List_Lines[key] = value
        return List_Lines



    # متد ساخت اکانت 
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
            print(f"=====================================================")
            print(f"{Phone} added .")
            print(f"=====================================================")
        else:
            print(f"=====================================================")
            print(f"{Phone} Number Exists")
            print(f"=====================================================")
        account.__remove_empty_lines()

    #متد سرچ کردن  
    def search(location_status,data):

        mydict = account.__Convert_DATA()
        global search_Pointer
        search_Pointer = 0
        for key,value in mydict.items():
                    if location_status in value["location_status"] and data in value["Name"]:
                        print(f"==================={value['Name']}===================")
                        print(f"Account ID : {key}\nLocation_Status : {value['location_status']}\nName : {value['Name']}\nPhone : {value['Phone']}\nAddress : {value['Address']}")
                        print(f"=====================================================")
                        search_Pointer += 1
                    elif location_status in value["location_status"] and data in value["Phone"]:
                        print(f"==================={value['Name']}===================")
                        print(f"Account ID : {key}\nLocation_Status : {value['location_status']}\nName : {value['Name']}\nPhone : {value['Phone']}\nAddress : {value['Address']}")
                        print(f"=====================================================")
                        search_Pointer += 1
                    elif location_status in value["location_status"] and data in value["Address"]:
                        print(f"==================={value['Name']}===================")
                        print(f"Account ID : {key}\nLocation_Status : {value['location_status']}\nName : {value['Name']}\nPhone : {value['Phone']}\nAddress : {value['Address']}")
                        print(f"=====================================================")
                        search_Pointer += 1
        if search_Pointer == 0:
            print(f"=====================================================")
        account.__remove_empty_lines()

    def delete(location_status: str,data: str):
        Listed_DATA = account.__Convert_DATA()
        account.search(location_status,data)
        list_ID = list(Listed_DATA.keys())
        while True:
                if search_Pointer == 0:
                    break
                try:
                    ask = int(input("Enter which account you want delete (By Account ID) : "))
                    if ask in list_ID:
                        del Listed_DATA[ask]
                        with open(DATABASE,'w') as file:
                            for value in Listed_DATA.values():
                                file.write(f"{str(value)}\n")
                        print(f"=====================================================")
                        print(f"Account ID : {ask} Successfully deleted. ")
                        print(f"=====================================================")
                        account.__remove_empty_lines()
                        break
                    else:
                        print(f"=====================================================")
                        print(f"{ask} not found, please try again.")
                        print(f"=====================================================")

                except ValueError:
                    print(f"=====================================================")
                    print("Please enter Only number not string")
                    print(f"=====================================================")
    

    def edit(location_status: str,data: str):
        Listed_DATA = account.__Convert_DATA()
        account.search(location_status,data)
        list_ID = list(Listed_DATA.keys())
        while True:
                if search_Pointer == 0:
                    break
                try:
                    ask = int(input("Enter which account you want edit (By Account ID) : "))
                    if ask in list_ID:
                        choosed_account: dict = Listed_DATA[ask]
                        print(f"=====================================================")
                        print("choose what data do you want to change")
                        print("1.Location_status\n2.Name,\n3.Phone\n4.Address\n5.all the datas in account")
                        option = int(input("Enter which data do you want to change :"))
                        match option:
                            case 1:
                                while True:
                                    try:
                                        print(f"=====================================================")
                                        print("1.Residental\n2.Office\n3.Markets")
                                        location_status = int(input("Enter location status :"))
                                        match location_status:
                                            case 1:
                                                location_status = "residental"
                                                break
                                            case 2:
                                                location_status = "office"
                                                break
                                            case 3:
                                                location_status = "markets"
                                                break
                                            case value:
                                                print("Please Enter betweens option")
                                    except ValueError:
                                        print("Please Enter only number")
                                        print("-----------------------")
                                choosed_account["location_status"] = location_status
                                with open(DATABASE,'w') as file:
                                    for value in Listed_DATA.values():
                                        file.write(f"{str(value)}\n")
                                print("All The Changes Applied.")

                            case 2:
                                New_Name = input("Enter name you want to change : ")
                                choosed_account["Name"] = New_Name.lower()
                                with open(DATABASE,'w') as file:
                                    for value in Listed_DATA.values():
                                        file.write(f"{str(value)}\n")
                                print("All The Changes Applied.")
                            case 3:
                                while True:
                                    try:
                                        New_Phone = input("Enter phone you want to change : ")
                                        if New_Phone[0] == "0":
                                            New_Phone = New_Phone.replace(New_Phone[0],"")
                                            int(New_Phone)
                                        else:
                                            int(New_Phone)
                                        New_Phone = str(New_Phone)
                                        New_Phone = "0" + New_Phone
                                        if len(New_Phone) == 11:
                                            break
                                        else:
                                            print("please enter correct number (11 digit)")
                                    except ValueError:
                                        print("Please Enter a number not string")
                                        print("====================================")
                                choosed_account["Phone"] = New_Phone
                                with open(DATABASE,'w') as file:
                                    for value in Listed_DATA.values():
                                        file.write(f"{str(value)}\n")
                                print("All The Changes Applied.")

                            case 4:
                                New_Address = input("Enter address you want to change : ")
                                choosed_account["Address"] = New_Address.lower()
                                with open(DATABASE,'w') as file:
                                    for value in Listed_DATA.values():
                                        file.write(f"{str(value)}\n")
                                print("All The Changes Applied.")
                            case 5:
                                while True:
                                    try:
                                        print("-------------------------")
                                        print("1.Residental\n2.Office\n3.Markets")
                                        location_status = int(input("Enter location status :"))
                                        match location_status:
                                            case 1:
                                                location_status = "residental"
                                                break
                                            case 2:
                                                location_status = "office"
                                                break
                                            case 3:
                                                location_status = "markets"
                                                break
                                            case value:
                                                print("Please Enter betweens option")
                                    except ValueError:
                                        print("Please Enter only number")
                                        print("-----------------------")

                                New_Name = input("Enter name you want to change : ")
                                while True:
                                    try:
                                        New_Phone = input("Enter phone you want to change : ")
                                        if New_Phone[0] == "0":
                                            New_Phone = New_Phone.replace(New_Phone[0],"")
                                            int(New_Phone)
                                        else:
                                            int(New_Phone)
                                        New_Phone = str(New_Phone)
                                        New_Phone = "0" + New_Phone
                                        if len(New_Phone) == 11:
                                            break
                                        else:
                                            print("please enter correct number (11 digit)")
                                    except ValueError:
                                        print("Please Enter a number not string")
                                        print("====================================")
                                New_Address = input("Enter address you want to change : ")

                                choosed_account["location_status"] = location_status
                                choosed_account["Address"] = New_Address.lower()
                                choosed_account["Phone"] = New_Phone.lower()
                                choosed_account["Name"] = New_Name.lower()

                                with open(DATABASE,'w') as file:
                                    for value in Listed_DATA.values():
                                        file.write(f"{str(value)}\n")
                                print("All The Changes Applied.")



                            case value:
                                print("please choose between options.")
                            
                        print(f"Account ID : {ask} Successfully edited. ")
                        account.__remove_empty_lines()
                        break
                    else:
                        print(f"{ask} not found, please try again.")
                except ValueError:
                    print("Please enter Only number not string")



           

print("-------------------------------")
print("Welcome to Oprator 118 Account")

while True:
    print("-------------------------------")
    print("1.search Accounts\n2.create Account\n3.edit Account\n4.delete Account\n5.list Account\n6.exit")
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
                while True:
                    try:
                        print("--------------------------")
                        print("1.Residental\n2.Office\n3.Markets\n4.all types")
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
                            case 4: 
                                location_status = ""
                                break
                            case value:
                                print("please choose between options.")
                    except ValueError:
                        print("Please Enter a number not string")
                        print("====================================")
                location_status = location_status.lower()
                data = input("search by Name/Address/Phone :").lower()
                account.edit(location_status,data)
            case 4:
                while True:
                    try:
                        print("--------------------------")
                        print("1.Residental\n2.Office\n3.Markets\n4.all types")
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
                            case 4: 
                                location_status = ""
                                break
                            case value:
                                print("please choose between options.")
                    except ValueError:
                        print("Please Enter a number not string")
                        print("====================================")
                location_status = location_status.lower()
                data = input("search by Name/Address/Phone :").lower()
                account.delete(location_status,data)
            case 5:
                account.search("","")
                cont = input("")
            case 6:
                print("see you later...👋👋👋")
                exit()
            case value:
                print(f" {value} not in the option list")
                print("-------------------------------")
    except ValueError:
        print("please choose option(number only)")
        print("-------------------------------")

    