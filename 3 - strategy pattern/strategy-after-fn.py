import string
import random
from typing import List, Callable


def generate_id(length=8):
    # helper function for generating an id
    return ''.join(random.choices(string.ascii_uppercase, k=length))


class Ticket_Soporte:

    def __init__(self, customer, issue):
        self.id = generate_id()
        self.customer = customer
        self.issue = issue


def fifoOrdering(list: List[Ticket_Soporte]) -> List[Ticket_Soporte]:
    return list.copy()


def filoOrdering(list: List[Ticket_Soporte]) -> List[Ticket_Soporte]:
    list_copy = list.copy()
    list_copy.reverse()
    return list_copy


def randomOrdering(list: List[Ticket_Soporte]) -> List[Ticket_Soporte]:
    list_copy = list.copy()
    random.shuffle(list_copy)
    return list_copy


def blackHoleOrdering(list: List[Ticket_Soporte]) -> List[Ticket_Soporte]:
    return []


class Soporte_Cliente:

    def __init__(self):
        self.tickets = []

    def create_ticket(self, customer, issue):
        self.tickets.append(Ticket_Soporte(customer, issue))

    def process_tickets(self, ordering: Callable[[List[Ticket_Soporte]], List[Ticket_Soporte]]):
        # create the ordered list
        ticket_list = ordering(self.tickets)

        # if it's empty, don't do anything
        if len(ticket_list) == 0:
            print("There are no tickets to process. Well done!")
            return

        # go through the tickets in the list
        for ticket in ticket_list:
            self.process_ticket(ticket)

    def process_ticket(self, ticket: Ticket_Soporte):
        print("==================================")
        print(f"Processing ticket id: {ticket.id}")
        print(f"Customer: {ticket.customer}")
        print(f"Issue: {ticket.issue}")
        print("==================================")


# create the application
app = Soporte_Cliente()

# register a few tickets
app.create_ticket("John Smith", "My computer makes strange sounds!")
app.create_ticket("Linus Sebastian", "I can't upload any videos, please help.")
app.create_ticket("Arjan Egges", "VSCode doesn't automatically solve my bugs.")

# process the tickets
app.process_tickets(blackHoleOrdering)
