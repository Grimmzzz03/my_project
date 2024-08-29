# check username from website
import re
url = input("Enter URL:").strip()

if matches:= re.search(r"^https?://(?:www\.)?twitter\.com/([a-zA-Z0-9_]+)", url, re.IGNORECASE):
    print(f"USERNAME: ", matches.group(1))