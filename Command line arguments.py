# Command line arguments
import sys

"""
if len(sys.argv) ==1:
    sys.exit("Not enough arguments")
    
elif len(sys.argv) > 2:
    sys.exit("Too many arguments")
    
else:
    sys.exit("my name is", sys.argv[1])
"""

if len(sys.argv) < 2:
    sys.exit("Not enough arguments")
    
for arg in sys.argv[1:]:
    print("my name is: ", arg)
    
    
    
