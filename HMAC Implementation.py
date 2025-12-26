import hmac
import hashlib

# Define the student ID
student_id = "11735527"  #ID
key_hex = (student_id * 8)[:64]  # Repeat it 8 times
key = bytes.fromhex(key_hex)  # Convert to bytes

# Write the message to a file named 'message.txt'
message = "Pay $1000 to Bob"
with open("message.txt", "w") as msg_file:
    msg_file.write(message)

# Read and display the message file
with open("message.txt", "r") as msg_file:
    print("Message file contents:")
    print(msg_file.read())

# Compute HMAC-SHA256
hmac_obj = hmac.new(key, message.encode(), hashlib.sha256)
tag_hex = hmac_obj.hexdigest()

# Write the authentication tag to a file
with open("tag.txt", "w") as tag_file:
    tag_file.write(tag_hex)

# Display the authentication tag
print("\nGenerated HMAC-SHA256 tag:")
print(tag_hex)

# Verification process
with open("tag.txt", "r") as tag_file:
    stored_tag = tag_file.read().strip()

# Verify the tag
hmac_verify = hmac.new(key, message.encode(), hashlib.sha256).hexdigest()
if hmac.compare_digest(stored_tag, hmac_verify):
    print("\nVerification succeeded: The tag is valid.")
else:
    print("\nVerification failed: The tag does not match.")
