
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

# Define the student ID
student_id = "11735527"  #ID
key_hex = (student_id * 8)[:64]  # Repeat it 8 times to get 256 bits
key = bytes.fromhex(key_hex)  # Convert to bytes

# Write the message to "message.txt"
message = "Pay $1000 to Bob"
with open("message.txt", "w") as msg_file:
    msg_file.write(message)

# Read and display "message.txt"
with open("message.txt", "r") as msg_file:
    print("\nOriginal Message (message.txt):")
    print(msg_file.read())

# Encrypt using AES-256-GCM
nonce = get_random_bytes(12)  # 96-bit nonce
cipher = AES.new(key, AES.MODE_GCM, nonce=nonce)
ciphertext, tag = cipher.encrypt_and_digest(message.encode())

# Save ciphertext and tag to "ciphertext.txt"
with open("ciphertext.txt", "w") as cipher_file:
    cipher_file.write(f"Nonce: {nonce.hex()}\n")
    cipher_file.write(f"Ciphertext: {ciphertext.hex()}\n")
    cipher_file.write(f"Tag: {tag.hex()}\n")

# Display ciphertext and tag
print("\nCiphertext and Tag (ciphertext.txt):")
print(f"Nonce: {nonce.hex()}")
print(f"Ciphertext: {ciphertext.hex()}")
print(f"Tag: {tag.hex()}")

# Decrypt and verify
with open("ciphertext.txt", "r") as cipher_file:
    lines = cipher_file.readlines()
    nonce = bytes.fromhex(lines[0].split(": ")[1].strip())
    ciphertext = bytes.fromhex(lines[1].split(": ")[1].strip())
    tag = bytes.fromhex(lines[2].split(": ")[1].strip())

# Attempt to decrypt
try:
    cipher = AES.new(key, AES.MODE_GCM, nonce=nonce)
    decrypted_message = cipher.decrypt_and_verify(ciphertext, tag)
    print("\nDecryption successful! The message is:")
    print(decrypted_message.decode())
except ValueError:
    print("\nCiphertext rejected.")
