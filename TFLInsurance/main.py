from customer.customer import Customer
from policy.policy import Policy


# Create Customer
customer = Customer(
    101,
    "Rohit",
    "rohit@gmail.com"
)

customer.display_customer()


print("--------------------")


# Create Policy
policy = Policy(
    "POL1001",
    101,
    "Motor Insurance",
    25000
)

policy.display_policy()

print("Calculated Premium:", policy.calculate_premium())