# Libraries
import random

coin = random.choice(["heads", "tails"])
print(f"The coin landed on: {coin} side\n") # print(coin)


cards = (["king", "queen", "jack"])
random.shuffle(cards)
for card in cards:
    print(f"{card}")


number = random.randint(1, 10)
print(f"\nRandom number between 1 and 10: {number}")

