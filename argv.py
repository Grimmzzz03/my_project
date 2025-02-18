import sys

def total(*numbers):
    sum = 0
    for i in numbers:
        sum += i
    return sum

num = [int (x) for x in sys.argv[1:]]
r = total(*num)
print(r)
