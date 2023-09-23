DATABASE = "database.txt"

class account:

    DATABASE_DICT = {
            "Name":"",
            "Phone":"",
            "Address":"",
    }

    def create(Name: str,Phone: int,Address: str):
        # information of account 
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
                Name = input("Enter the name :")
                Phone = input("Enter Phone number :")
                Address = input("Enter Address :")

                account.create(Name,Phone,Address)
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

    