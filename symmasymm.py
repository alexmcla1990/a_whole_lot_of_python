#install cryptography

from cryptography.fernet import Fernet


message = 'whatsupdude'

key=Fernet.generate_key()
print(key)

fernet_obj= Fernet(key)

encrypted_message=fernet_obj.encrypt(message.encode())
print(encrypted_message)

decrypted_message=fernet_obj.decrypt(encrypted_message).decode()
print(decrypted_message)

with open('test.txt', 'w') as file: 
    file.write(encrypted_message)