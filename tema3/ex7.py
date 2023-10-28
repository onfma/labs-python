# Write a function that receives a variable number of sets and returns a dictionary 
# with the following operations from all sets two by two: reunion, intersection, a-b, b-a. 
# The key will have the following form: "a op b", where a and b are two sets, and op is the applied operator: |, &, -. 

def set_operations(*args):
    operations = {}

    for i, set_a in enumerate(args):
        for j, set_b in enumerate(args):
            if i != j:
                key = f"{set_a} | {set_b}"
                operations[key] = set_a | set_b

                key = f"{set_a} & {set_b}"
                operations[key] = set_a & set_b

                key = f"{set_a} - {set_b}"
                operations[key] = set_a - set_b

                key = f"{set_b} - {set_a}"
                operations[key] = set_b - set_a

    return operations

# Example usage:
result = set_operations({1, 2}, {2, 3})

for key, value in result.items():
    print(f"{key}: {value}")
