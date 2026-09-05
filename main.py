budget = float(input("What is your PC budget? $"))
cpu = float(input("How much does your CPU cost? $"))
gpu = float(input("How much does your GPU cost? $"))
ram = float(input("How much does your RAM cost? $"))
motherboard = float(input("How much does your Motherboard cost? $"))
storage = float(input("How much does your Storage cost? $"))
power_supply = float(input("How much does your Power Supply cost? $"))
case = float(input("How much does your Case cost? $"))


total_cost = cpu + gpu + ram + motherboard + storage + power_supply + case

remaining_budget = budget - total_cost


print(f"Total Build Cost: ${total_cost:.2f}")
print(f"Remaining Budget: ${remaining_budget:.2f}")


if remaining_budget > 0:
    print(f"You are within budget with ${remaining_budget:.2f} remaining!")

elif remaining_budget == 0:
    print("You used your entire budget!")

else:
    print(f"You are over budget by ${abs(remaining_budget):.2f}!")