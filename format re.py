# format re
import re

name = input("Enter the your name: ").strip()

if matches:= re.search(r"^(.+), *(.+)$", name):
    name = matches.group(1) + " " + matches.group(2)
    
print(f"hello, {name}")
