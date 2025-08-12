# ask email from use 

email = input("Enter your email: ").strip()


# username, domain = email.split("@")

# if (username) and ("." in domain):
#     print("valid")
# else:
#     print("invalid")

# Python library to check regular expression

import re

if re.search(r".+@.+\.", email):
    print("valid")
else:
    print("invalid")