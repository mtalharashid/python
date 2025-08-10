import re

name =  input("enter your name: ").strip()

if matches := re.search(r"^(.+), *(.+)$", name):
    first, last = matches.groups()
    name = f"{first} {last}"

print(f"hello: {name}")