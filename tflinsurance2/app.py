# JSON TO PYTHON


# import json
# with open("policies.json", "r") as file:
#     policies = json.load(file)

# print(policies)


#  PYTHON TO JSON 


#  import json

# policy = {
#     "policy_number": "POL1003",
#     "customer_name": "sakshi",
#     "premium": 18000,
#     "status": "Active"
# }

# with open("policies.json", "w") as file:
#     json.dump(policy, file, indent=4)


# ADD LIST


# import json

# with open("policies.json", "r") as file:
#     policies = json.load(file)

# new_policy = {
#     "policy_number": "POL1004",
#     "customer_name": "Amit",
#     "premium": 18000,
#     "status": "Active"
# }

# policies.append(new_policy)

# with open("policies.json", "w") as file:
#     json.dump(policies, file, indent=4)


# FIND POLICY


# import json

# def find_policy(policy_number):

#     with open("policies.json", "r") as file:
#         policies = json.load(file)

#     for policy in policies:

#         if policy["policy_number"] == policy_number:
#             return policy

#     return None

# policy = find_policy("POL1001")

# print(policy)


# FILE DOESNT EXIST

# import json

# try:

#     with open("policies.json", "r") as file:
#         policies = json.load(file)

# except FileNotFoundError:

#     print("Policy file does not exist.")
#     policies = []




# import json

# try:

#     with open("policies.json", "r") as file:
#         policies = json.load(file)

# except FileNotFoundError:

#     print("Policy file not found.")
#     policies = []

# except json.JSONDecodeError:

#     print("Policy file contains invalid JSON.")
#     policies = []


# count references 
                                                  
# import sys

# policy = {
#     "policy_id": "POL1001",
#     "customer": "Ravi",
#     "coverage": 1000000
# }


# policy_2=policy

# print(sys.getrefcount(policy))


# circular references 

import gc

class Customer:
    pass


class Policy:
    pass



customer = Customer()
policy = Policy()

customer.policy = policy
policy.customer = customer

del customer
del policy

collected = gc.collect()

