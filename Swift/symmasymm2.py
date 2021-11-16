import rsafrom rsa.key import PrivateKey, PublicKey

message = "suhdude"

publicKey, privateKey = rsa.newkeys(512)
print(publicKey,privateKey)

encryption_message=rsa.encrypt(message.encode(), publicKey)
print(encryption_message)

decrypt_message= rsa.decrypt(message.encode(), publicKey)
print(decrypt_message)

decrypt_message=rsa.decrypt(encryption_message, privateKey).decode()
print(encryption_message)