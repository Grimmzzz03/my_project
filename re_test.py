import re

"""
text = 'there is the phone number 123456 in this row and age: 23'
match = re.search(r'\d+',text)
match_age = re.search(r'age: (\d+)',text)
match_num = re.findall(r'\d+',text)
if match:
    print(match.group(0))

if match_age:
    print(match_age.group(0))

if match_num:
    print(match_num)
    
print("1--------")

cases = [
    "hello!",
    "hello world.",
    "hello,world",
    ".",
]

for case in cases:
    print(case)
    match = re.search(r'.',case)
    if match:
        print(match.group(0))
        
print("2--------")

for case in cases:
    print(case)
    match = re.search(r'\.',case)
    if match:
        print(match.group(0))

print("3--------")

for case in cases:
    print(case)
    match = re.search(r'[.]',case)
    if match:
        print(match.group(0))
"""        
"""
strings = (
    "-a-",
    "-b-",
    "-c-",
    "-x-",
    "-aa-",
    "-ab-",
    "--",
    "-abc-",
    "-ax-",
    "-ay-",
    "-az-",
    "-ba-",
    "-bb-",
    "-bc-",
    "-ca-",
    "-cb-",
    "-cc-",
    "-da-",
    "-db-",)

for line in strings:
    match = re.search(r'-[abc]-', line)
    if match:
        print(line)

print('1=========================')

for line in strings:
    match = re.search(r'-[abc]+-', line)
    if match:
        print(line)

print('2=========================')

for line in strings:
    match = re.search(r'-[abc]*-', line)
    if match:
        print(line)
"""

# code to fix date using re.sub

dates = {
    "2021-1-1": "2021-01-01",
    "2021-2-10": "2021-02-10",
    "2021-3-5": "2021-03-05"
}

def fix_date(date):
    """ Fix a date string by padding single digit month or day with a zero.
    
    Args:
        date (str): A date string in the format 'YYYY-MM-DD'
    
    Returns:
        str: The corrected date string
    """
    return re.sub(r'-(\d)\b', r'-0\1',date)

for original in sorted(dates.keys()):
    result = fix_date(original)
    
    if result != dates[original]:
        print(f" old: {original}")
        print(f"new: {result}")
        print(f"expected: {dates[original]}")


