while True:
    try:
        budget = float(input("What is your PC budget? $"))
        break
    except ValueError:
        print("Please enter a valid number.")

parts = {}

component_names = [
    "CPU",
    "GPU",
    "RAM",
    "Motherboard",
    "Storage",
    "Power Supply",
    "Case"
]

for component in component_names:
    while True:
        try:
            price = float(input(f"How much does your {component} cost? $"))
            parts[component] = price
            break
        except ValueError:
            print("Please enter a valid number.")

total_cost = sum(parts.values())
remaining_budget = budget - total_cost

print("\n--- Build Summary ---")

for component, price in parts.items():
    print(f"{component}: ${price:.2f}")

print(f"\nTotal Build Cost: ${total_cost:.2f}")
print(f"Remaining Budget: ${remaining_budget:.2f}")

if remaining_budget > 0:
    print(f"You are within budget with ${remaining_budget:.2f} remaining!")
elif remaining_budget == 0:
    print("You used your entire budget!")
else:
    print(f"You are over budget by ${abs(remaining_budget):.2f}!")