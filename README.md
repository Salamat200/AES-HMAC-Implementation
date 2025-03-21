## Installation
- **Pycryptodome** can be installed and accessed through:
  - **Library**: Go to Settings > Python Interpreter > Search for 'pycryptodome'.
  - **Command**: Use `pip install pycryptodome`.

## To Generate the Keys and Save in Separate Files

### Import ECC from Crypto.PublicKey
#### This allows us to generate and work with ECC keys.
     from Crypto.PublicKey import ECC

### Generate ECDSA key pair 
#### (This helps create a private key and a corresponding public key)
    key = ECC.generate(curve='P-256')

### Save private key in a file named private_key.pem 
#### This creates the file. "wt" means to save in text mode
    with open("private_key.pem", "wt") as f:
    f.write(key.export_key(format="PEM"))

### Save public key in a file named public_key.pem 
#### This creates the file."wt" means to save in text mode
    with open("public_key.pem", "wt") as f:
    f.write(key.public_key().export_key(format="PEM"))

### To signify that the key pair has been generated and saved successfully
    print("Keys generated successfully.")

## To Sign the Product

### Required Modules are imported
    import base64
    from Crypto.Signature import DSS
    from Crypto.Hash import SHA256
    from Crypto.PublicKey import ECC

### Read the product code from the file named "product.py"
    with open("product.py", "rb") as f:
    product_data = f.read()

### Generate hash function of product_data 
#### This results in a cryptographic digest of the file
    hash_obj = SHA256.new(product_data)

### open the previously generated private key file in text read mode "rt"
    with open("private_key.pem", "rt") as f:
    private_key = ECC.import_key(f.read())

### Sign the hash
    signer = DSS.new(private_key, 'fips-186-3')
    signature = signer.sign(hash_obj)

### Encode in Base64 (An option)
#### This converts the raw binary into Base64 format
    signature_b64 = base64.b64encode(signature)

### Save the signature
    with open("signature.ecdsa", "wb") as f:
    f.write(signature_b64)

### To confirm that the file has been signed and the signature has been saved
    print("Product signed successfully.")

## Verify The Signature

### Open public key file
     with open("public_key.pem", "rt") as f:
     public_key = ECC.import_key(f.read()) 

### Open product.py
    with open("product.py", "rb") as f: 
    product_data = f.read() 

### Open the saved signature file (signature.ecdsa)
    with open("signature.ecdsa", "rb") as f: 
    signature_b64 = f.read() 

### Convert the Base64-encoded signature to the original binary format
    signature = base64.b64decode(signature_b64)

### Generates SHA-256 hash of product.py
    hash_obj = SHA256.new(product_data)

### Verify the signature using the public key
    verifier = DSS.new(public_key, 'fips-186-3')

### try:
    verifier.verify(hash_obj, signature) 
### If valid
    print("Code certificate valid: execution allowed")
     exec(product_data.decode())

### except ValueError:
    print("Code certificate invalid: execution denied")