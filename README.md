# AES-256-GCM & HMAC Security Implementation

## Installation
Install the required library using: `pip install pycryptodome`

## Overview
This project demonstrates authenticated encryption using **AES-256-GCM** and message integrity verification using **HMAC-SHA256**. It includes both proper implementations and security testing to show how tampering is detected.

## Implementations

### AES-256-GCM Encryption & Decryption
This implements authenticated encryption with AES-256 in GCM mode
```python
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

# Define key from student ID
student_id = "11735527"
key_hex = (student_id * 8)[:64]
key = bytes.fromhex(key_hex)

# Encrypt with GCM mode
nonce = get_random_bytes(12)
cipher = AES.new(key, AES.MODE_GCM, nonce=nonce)
ciphertext, tag = cipher.encrypt_and_digest(message.encode())

# Decrypt and verify
cipher = AES.new(key, AES.MODE_GCM, nonce=nonce)
decrypted_message = cipher.decrypt_and_verify(ciphertext, tag)

import hmac
import hashlib

# Generate HMAC tag
hmac_obj = hmac.new(key, message.encode(), hashlib.sha256)
tag_hex = hmac_obj.hexdigest()

# Verify HMAC tag
hmac_verify = hmac.new(key, message.encode(), hashlib.sha256).hexdigest()
if hmac.compare_digest(stored_tag, hmac_verify):
    print("Verification succeeded")

# Test 1: Modify ciphertext (keeps same tag)
modified_ciphertext_hex = modify_first_char(ciphertext_hex)

# Test 2: Modify tag (keeps same ciphertext)
modified_tag_hex = modify_first_char(tag_hex)

# Both attempts will fail with ValueError
# GCM detects any tampering with ciphertext or tag

# Test 1: Copy and verify original message
shutil.copy("message.txt", "message1.txt")
# Verification succeeds

# Test 2: Modify message content
modified_message = "Pay $2000 to Bob"
# Verification fails

# Test 3: Tamper with stored tag
tampered_tag = ('0' if stored_tag[0] != '0' else '1') + stored_tag[1:]
# Verification fails

