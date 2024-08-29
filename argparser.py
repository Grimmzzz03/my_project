# argparser.add_argument
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-n", default=1, help = "no of times to print", type = int)
args = parser.parse_args()

for _ in range(args.n):
    print("Hello, World!")