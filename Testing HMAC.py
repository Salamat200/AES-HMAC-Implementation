import hmac
import hashlib
import shutil

# Define the student ID 
student_id = "11735527"  #ID
key_hex = (student_id * 8)[:64]  # Repeat it 8 times
key = bytes.fromhex(key_hex)  # Convert to bytes

# a. Copy "message.txt" to "message1.txt"
shutil.copy("message.txt", "message1.txt")

# Read and display "message1.txt"
with open("message1.txt", "r") as msg_file:
    message1 = msg_file.read()
print("\nCopied file 'message1.txt' contents:")
print(message1)

# Read and display the stored tag
with open("tag.txt", "r") as tag_file:
    stored_tag = tag_file.read().strip()
print("\nStored HMAC tag from 'tag.txt':")
print(stored_tag)

# Verify the tag with the copied file
hmac_verify = hmac.new(key, message1.encode(), hashlib.sha256).hexdigest()
if hmac.compare_digest(stored_tag, hmac_verify):
    print("\nVerification succeeded: The tag is valid.")
else:
    print("\nVerification failed: The tag does not match.")

# b. Modify "message1.txt" to change the payment amount
modified_message = "Pay $2000 to Bob"
with open("message1.txt", "w") as msg_file:
    msg_file.write(modified_message)

# Read and display the modified file
with open("message1.txt", "r") as msg_file:
    modified_content = msg_file.read()
print("\nModified file 'message1.txt' contents:")
print(modified_content)

# Verify the tag with the modified file
hmac_verify_modified = hmac.new(key, modified_content.encode(), hashlib.sha256).hexdigest()
if hmac.compare_digest(stored_tag, hmac_verify_modified):
    print("\nVerification succeeded: The tag is valid.")
else:
    print("\nVerification failed: The tag does not match.")

# c. Modify the stored tag by changing the first hex character
tampered_tag = ('0' if stored_tag[0] != '0' else '1') + stored_tag[1:]

# Verify the tampered tag with the original message
with open("message.txt", "r") as msg_file:
    original_message = msg_file.read()

hmac_verify_original = hmac.new(key, original_message.encode(), hashlib.sha256).hexdigest()
if hmac.compare_digest(tampered_tag, hmac_verify_original):
    print("\nVerification succeeded: The tag is valid.")
else:
    print("\nVerification failed: The tag does not match.")

