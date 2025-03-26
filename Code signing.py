#To import ECC from Crypto.PublicKey ( this allows us to generate and work with ECC keys)
from Crypto.PublicKey import ECC

# Generate ECDSA key pair (This helps create a private key and a corresponding public key)
key = ECC.generate(curve='P-256')

# Save private key in a file named private_key.pem (It creates the file)
with open("private_key.pem", "wt") as f: #"wt" means to save in text mode
    f.write(key.export_key(format="PEM")) #this converts the private key into PEM format

# Save public key in a file named public_key.pem (It creates the file)
with open("public_key.pem", "wt") as f: #"wt" means to save in text mode
    f.write(key.public_key().export_key(format="PEM")) #this converts the public key into PEM format

#To signify that the key pair has been generated and saved successfully
print("Keys generated successfully.")
