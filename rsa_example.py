import rsa

# Generate private and public key
public_key , private_key = rsa.newkeys(1024)


# Save the keys in respective file  in keys folder
with open("keys/public_key.pem","wb") as f:
    f.write(public_key.save_pkcs1("PEM"))

with open("keys/private_key.pem","wb") as f:
    f.write(private_key.save_pkcs1("PEM"))



# Read key from file 
current_public_key = ""
current_private_key=""
with open("keys/public_key.pem","rb") as f:
    current_public_key = rsa.PublicKey.load_pkcs1(f.read())

with open("keys/private_key.pem","rb") as f:
    current_private_key = rsa.PrivateKey.load_pkcs1(f.read())


# Sample message to encript
message = " This is  a sample message for encription"

# Encript with public key 
encrypted_message = rsa.encrypt(message.encode(),current_public_key)

print(" Encripted Message",encrypted_message)


# Decrypt with private key 
decrypted_message = rsa.decrypt(encrypted_message,current_private_key)

print(" Encripted Message",encrypted_message)


print(" Orginal Message",message)

print(" Decryped Message",decrypted_message)
