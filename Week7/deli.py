sandwich_orders = ['ham', 'turkey', 'pastrami', 'cheese']
finished_sandwiches = []

while sandwich_orders:
    current = sandwich_orders.pop()
    print(f"I made your {current} sandwich.")
    finished_sandwiches.append(current)

print("\nThe following sandwiches were made:")
for sandwich in finished_sandwiches:
    print(sandwich)