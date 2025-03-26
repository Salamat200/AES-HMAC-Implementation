# print_public_key.py

# Step 1: Load the public key
with open("public_key.pem", "rt") as f:
    public_key = f.read()  # Read the public key content

# Step 2: Print the public key to the screen
print("Public Key obtained:")
print(public_key)
