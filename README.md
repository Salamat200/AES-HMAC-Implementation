# Installation
 - Pycryptodome is installed could be accessed:
   Library - setting> Python interpreter> search 'pycryptodome'
 - 
   Command - 'pip install pycryptodome'```

To Generate the keys and save in separate files

 To import ECC from Crypto.PublicKey (this allows us to generate and work with ECC keys)
 ```from Crypto.PublicKey import ECC```

 #Generate ECDSA key pair (This helps create a private key and a corresponding public key)
key = ECC.generate(curve='P-256')

# Save private key in a file named private_key.pem (It creates the file)
#"wt" means to save in text mode
```with open("private_key.pem", "wt") as f:``` 
#this converts the private key into PEM format
    ```f.write(key.export_key(format="PEM"))``` 

# Save public key in a file named public_key.pem (It creates the file)
#"wt" means to save in text mode
```with open("public_key.pem", "wt") as f:```
#this converts the public key into PEM format
    ```f.write(key.public_key().export_key(format="PEM"))``` 

#To signify that the key pair has been generated and saved successfully
print("Keys generated successfully.")```

# To Sign the Product

# Required Modules are imported
'''import base64
from Crypto.Signature import DSS
from Crypto.Hash import SHA256
from Crypto.PublicKey import ECC

# Read the product code from the file named "product.py"
with open("product.py", "rb") as f: # "rb" means in binary read mode
    product_data = f.read() # the content of the file is read into the product_data variable

# Generate hash function of product_data (this results in a cryptographic digest of the file)
hash_obj = SHA256.new(product_data)

# opens the previously generated private key file in text read mode "rt"
with open("private_key.pem", "rt") as f:
    private_key = ECC.import_key(f.read()) #the Key is read and imported into private_key variable

# Sign the hash
signer = DSS.new(private_key, 'fips-186-3') #This creates a new DSS signer object with the private key. FIPS 186-3 is to set security standards
signature = signer.sign(hash_obj) # To generate a digital signature for the hash

# Encode in Base64 (An option)
signature_b64 = base64.b64encode(signature) # Converts the raw binary into Base64 format while the signature remains a bytes object

# Save the signature
with open("signature.ecdsa", "wb") as f:  # "wb" mode ensures it's written as bytes
    f.write(signature_b64) # The Base64-encoded signature is written to the file

# To confirm that the file has been signed and the signature has been saved
print("Product signed successfully.")

Verify the Signature

# Open public key file
'''with open("public_key.pem", "rt") as f: # in text read mode 'rt'
    public_key = ECC.import_key(f.read()) # The key is read and imported into public_key

# Open product.py
with open("product.py", "rb") as f: # in binary read mode 'rb'
    product_data = f.read() # The entire content is read into product_data

# Open the saved signature file (signature.ecdsa)
with open("signature.ecdsa", "rb") as f: # In binary read mode 'rb'
    signature_b64 = f.read() # The Base64-encoded signature is read into signature_b64

# Convert the Base64-encoded signature to the original binary format
signature = base64.b64decode(signature_b64)

# Generates SHA-256 hash of product.py
hash_obj = SHA256.new(product_data)

# Verify the signature using the public key
verifier = DSS.new(public_key, 'fips-186-3')

try:
    verifier.verify(hash_obj, signature) # Checks the validity of the hash of product.py
# If valid
    print("Code certificate valid: execution allowed")

# To execute product.py (if verification passes)
    exec(product_data.decode())

# If verification does not match, ValueError is raised
except ValueError:
    print("Code certificate invalid: execution denied")