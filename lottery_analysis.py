import random

"""
def get_winning_ticket(series):
    winning_ticket = []
    while len(winning_ticket) < 4:
        pulled_item = random.choice(series)

        if pulled_item not in winning_ticket:
            winning_ticket.append(pulled_item)

    return winning_ticket


def check_ticket(played_ticket,winning_ticket):
    if played_ticket == winning_ticket:
        return True
    else:
        return False

def make_random_ticket(series):
    ticket = []
    while len(ticket) < 4:
        pulled_item = random.choice(series)

        if pulled_item not in ticket:
            ticket.append(pulled_item)

    return ticket

series = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'a', 'b', 'c', 'd', 'e')
winning_ticket = get_winning_ticket(series)

plays = 0
won = False

max_tries = 1_000_000

while not won:
    new_ticket = make_random_ticket(series)
    won = check_ticket(new_ticket, winning_ticket)
    plays += 1
    if plays >= max_tries:
        break

if won:
    print("we have a winning ticket!")
    print(f"your ticket: {new_ticket}")
    print(f"winning ticket: {winning_ticket}")
    print(f"it only took {plays} tries to win!")
else:
    print(f"tried {plays} times, without pulling a winner. :(")
    print(f"your ticket: {new_ticket}")
    print(f"winning ticket: {winning_ticket}")
"""

"""
class Lottery:
    def __init__(self, series):
        self.series = series
        self.winning_ticket = self.get_winning_ticket()
        self.plays = 0
        self.won = False

    def get_winning_ticket(self):
        winning_ticket = []
        while len(winning_ticket) < 4:
            pulled_item = random.choice(self.series)

            if pulled_item not in winning_ticket:
                winning_ticket.append(pulled_item)

        return winning_ticket


    def check_ticket(self, played_ticket):
        if played_ticket == self.winning_ticket:
            return True
        else:
            return False


    def make_random_ticket(self):
        ticket = []
        while len(ticket) < 4:
            pulled_item = random.choice(self.series)

            if pulled_item not in ticket:
                ticket.append(pulled_item)

        return ticket

    def play(self):
        self.plays += 1
        new_ticket = self.make_random_ticket()
        self.won = self.check_ticket(new_ticket)
        if self.won:
            print("we have a winning ticket!")
            print(f"your ticket: {new_ticket}")
            print(f"winning ticket: {self.winning_ticket}")
            print(f"it only took {self.plays} tries to win!")
        else:
            print(f"tried {self.plays} times, without pulling a winner. :(")
            print(f"your ticket: {new_ticket}")
            print(f"winning ticket: {self.winning_ticket}")

        return self.won


series = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'a', 'b', 'c', 'd', 'e')
lottery = Lottery(series)

while not lottery.play():
    pass
"""
