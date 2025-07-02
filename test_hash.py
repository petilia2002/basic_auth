from werkzeug.security import generate_password_hash, check_password_hash

password = "12345"

password_hash = generate_password_hash(password, method="pbkdf2:sha256")

print(f"Password Before Hashing: {password}")
print(f"Password After Hashing: {password_hash}")

res = check_password_hash(password_hash, "12345")
print(res)
