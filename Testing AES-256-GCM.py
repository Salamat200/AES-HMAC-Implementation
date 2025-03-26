
# Read the original ciphertext.txt
with open("ciphertext.txt", "r") as cipher_file:
    lines = cipher_file.readlines()

nonce_hex = lines[0].split(": ")[1].strip()
ciphertext_hex = lines[1].split(": ")[1].strip()
tag_hex = lines[2].split(": ")[1].strip()

# Function to modify the first hex character
def modify_first_char(hex_str):
    first_char = hex_str[0]
    new_char = '1' if first_char != '1' else '2'  # Change the first hex character
    return new_char + hex_str[1:]

# a. Modify ciphertext and save as ciphertext1.txt
modified_ciphertext_hex = modify_first_char(ciphertext_hex)

with open("ciphertext1.txt", "w") as modified_cipher_file:
    modified_cipher_file.write(f"Nonce: {nonce_hex}\n")
    modified_cipher_file.write(f"Ciphertext: {modified_ciphertext_hex}\n")
    modified_cipher_file.write(f"Tag: {tag_hex}\n")

# Display modified ciphertext1.txt
print("\nModified 'ciphertext1.txt' (Ciphertext altered, Tag unchanged):")
with open("ciphertext1.txt", "r") as modified_cipher_file:
    print(modified_cipher_file.read())

# Attempt decryption with modified ciphertext
try:
    from Crypto.Cipher import AES

    # Define the student ID
    student_id = "11735527" # ID
    key_hex = (student_id * 8)[:64]  # Repeat it 8 times to get 256 bits
    key = bytes.fromhex((student_id * 8)[:64])  # Use the same key as before
    nonce = bytes.fromhex(nonce_hex)
    ciphertext = bytes.fromhex(modified_ciphertext_hex)
    tag = bytes.fromhex(tag_hex)

    cipher = AES.new(key, AES.MODE_GCM, nonce=nonce)
    decrypted_message = cipher.decrypt_and_verify(ciphertext, tag)
    print("\nDecryption successful! The message is:")
    print(decrypted_message.decode())
except ValueError:
    print("\nCiphertext rejected: Modified ciphertext caused decryption failure.")

# b. Modify the first character of the tag and save in ciphertext.txt
modified_tag_hex = modify_first_char(tag_hex)

with open("ciphertext.txt", "w") as modified_tag_file:
    modified_tag_file.write(f"Nonce: {nonce_hex}\n")
    modified_tag_file.write(f"Ciphertext: {ciphertext_hex}\n")
    modified_tag_file.write(f"Tag: {modified_tag_hex}\n")

# Display modified ciphertext.txt
print("\nModified 'ciphertext.txt' (Tag altered, Ciphertext unchanged):")
with open("ciphertext.txt", "r") as modified_tag_file:
    print(modified_tag_file.read())

# Attempt decryption with modified tag
try:
    ciphertext = bytes.fromhex(ciphertext_hex)
    tag = bytes.fromhex(modified_tag_hex)

    cipher = AES.new(key, AES.MODE_GCM, nonce=nonce)
    decrypted_message = cipher.decrypt_and_verify(ciphertext, tag)
    print("\nDecryption successful! The message is:")
    print(decrypted_message.decode())
except ValueError:
    print("\nCiphertext rejected: Modified tag caused authentication failure.")
