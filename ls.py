import os

class Permissions:
    
    READ = 0b1
    WRITE = 0b1<<1
    CREATE = 0b1<<2
    DELETE = 0b1<<3

user1 = {
    "name" : "Hemant",
    "role" : Permissions.READ | Permissions.WRITE
}
admin = {
    "name" : "Utkarsh",
    "role" : Permissions.CREATE | Permissions.READ | Permissions.WRITE | Permissions.DELETE
}


def myfunc(user,operation):
    if operation == "create":
        if Permissions.CREATE & user["role"] == Permissions.CREATE:
            open("binary.txt","w")
            print("File Created Successfully")
        else:
            print("Create Permission Required")

    elif operation == "read":
        if Permissions.READ & user["role"] == Permissions.READ:
            open("binary.txt","r")
            print("File open in Read Mode")

        else:
            print("Read Permission Required")

    elif operation == "write":
        if Permissions.WRITE & user["role"] == Permissions.WRITE:
            with open("binary.txt","w") as f:
                f.write("Heloo This is demo text")
                f.write("\n")
                print("Text is written")

        else:
            print("Write Permission Required")

    elif operation == "delete":
        if Permissions.DELETE & user["role"] == Permissions.DELETE:
            os.remove("binary.txt")
            print("File deleted ")

        else:
            print("Delete Permission required")
            



myfunc(admin,"create")
myfunc(admin,"read")

myfunc(user1,"write")

myfunc(user1,"delete")
myfunc(admin,"delete")

print(type(Permissions.READ))
print(bin(Permissions.READ))
print(bin(Permissions.WRITE))
print(bin(Permissions.CREATE))
print(bin(Permissions.DELETE))