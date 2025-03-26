# Required Modules are imported
import base64
from Crypto.Signature import DSS
from Crypto.Hash import SHA256
from Crypto.PublicKey import ECC

# Read the product code from the file named "product.py"
with open("Product.py", "rb") as f: # "rb" means in binary read mode
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

