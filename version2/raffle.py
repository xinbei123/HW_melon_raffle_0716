"""Randomly pick customer and print customer info"""

# Add code starting here

# Hint: remember to import any functions you need from
# other files or libraries
import random
from customers import get_customers_from_file

def pick_winner(customers):
    choosen_customer = random.choice(customers)

    print(f"Tell {choosen_customer.name} at {choosen_customer.email}"
           " that they've won.")

def run_raffle():
    """Run the weekly raffle."""

    customers = get_customers_from_file("customers.txt")
    pick_winner(customers)

if __name__ == '__main__':
    run_raffle


print(pick_winner(get_customers_from_file("customers.txt")))