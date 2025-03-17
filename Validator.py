# Importing required Modules
import base64
from Crypto.Signature import DSS
from Crypto.Hash import SHA256
from Crypto.PublicKey import ECC

# Open public key file
with open("public_key.pem", "rt") as f: # in text read mode 'rt'
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
