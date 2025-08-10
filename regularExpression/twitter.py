#  ask user twitter profile username and figuer out that the url

import re

url = input("twitter url? ").strip()

username = re.sub(r"^(https?://)?(www\.)?twitter\.com/", "", url)

print(f"username: {username}")