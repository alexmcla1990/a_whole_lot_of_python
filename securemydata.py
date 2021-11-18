import hashlib
import uuid


h = hashlib.md5()
f = open(str(uuid.uuid4()) + ".txt", "w")



def encode (data, shift):
    encoded = ""

    for i in range(len(data)):
        
        char = data[i]
        if (char.isupper()):
            encoded += chr((ord(char) + shift -65) % 26 +65)
        elif (char.islower()):
            encoded += chr((ord(char) + shift -97) % 26 +97)
        elif (char.isdigit()):
            number = (int(char) + shift) % 10
            encoded += str(number)
        else:
            encoded += char
    return encoded

def decode (data, shift):
    decoded = ""

    for i in range(len(data)):
        
        char = data[i]
        if (char.isupper()):
            decoded += chr((ord(char) - shift -65) % 26 +65)
        elif (char.islower()):
            decoded += chr((ord(char) - shift -97) % 26 +97)
        elif (char.isdigit()):
            number = (int(char) - shift) % 10
            decoded += str(number)
        else:
            decoded += char
    return decoded

menu = ""
while menu != '1' or menu != '2':
    menu = input("Would you like to save a new passw1ord or view your old ones?"
                    "\n 1. Input new patient."
                    "\n 2. View existing patient information."
                    "\n 3. Generate Password."
                    "\n 4. Save Passwords and Exit Program."
                    )
    if menu == "1":
        patientName = input("Enter name of patient:")
        healthPlanId = input("Enter Id of patient:")
        securityKey = input("Enter security key:")
        shift = 6
        file = open("secretinformation.txt", "a")
        file.write(encode(patientName, shift) +";|"+ encode(healthPlanId, shift) +";|"+ encode(securityKey, shift) + "\n")
        file.close()
    if menu == "2":
        file = open("secretinformation.txt", "r")
        print("Patient Name\t\tIdentification\t\tSecurity Key")
        for i in file:
            shift = 6
            data = i.split(";|")
            print(decode(data[0],shift)+"\t\t"+decode(data[1], shift)+"\t\t"+decode(data[2], shift))

    if menu == "3":
        with open('secretinformation.txt', 'rb') as afile:
            buf = afile.read()
            h.update(buf)
            print(h.hexdigest(), file=f)
            print('Hash Generated')
           

        

    if menu == "4":
        exit()