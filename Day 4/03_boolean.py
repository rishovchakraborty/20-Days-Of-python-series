print(True)         # ➜ True
print(False)        # ➜ False
print(type(True))   # ➜ <class 'bool'>


print(bool(()))      # ➜ False (empty tuple)
print(bool(0))       # ➜ False (zero)
print(bool(""))      # ➜ False (empty string)
print(bool(None))    # ➜ False (None is always considered False)


email    = ""
phone    = "017-1234"
username = "hd"

# Allows registration if at least one field is filled
print(any([email, phone, username]))  # ➜ True

# Allows registration only if all fields are filled
print(all([email, phone, username]))  # ➜ False