# --- TRAVEL TRIP ESTIMATOR PROJECT ---

print("Hi! This is your travel guide.")
print("We offer info on Maldives, Switzerland, and Santorini.")

destination = input("Where do you want to travel? ").upper()

if destination == "MALDIVES":
    print("We have the Maldives Guide for you!")
    package = {
        "location": "Maldives, Indian Ocean",
        "budget": 2499,
        "duration": "7 days / 6 nights",
        "daily_budget": 120,
        "daily_mid": 280,
        "daily_luxury": 650
    }
    print(f"Location: {package['location']}, Price: ${package['budget']}, Duration: {package['duration']}")
    
    # Ask for customer preference
    tier = input("Choose a daily travel style (Budget, Mid-range, Luxury): ").lower()
    if tier == "budget":
        print(f"Estimated daily cost: ${package['daily_budget']}/day")
    elif tier == "mid-range" or tier == "mid":
        print(f"Estimated daily cost: ${package['daily_mid']}/day")
    elif tier == "luxury":
        print(f"Estimated daily cost: ${package['daily_luxury']}/day")
    else:
        print("Invalid choice, showing standard rates.")

elif destination == "SWITZERLAND":
    print("We have the Switzerland Guide for you!")
    package = {
        "location": "Zermatt, Switzerland",
        "budget": 1850,
        "duration": "5 days / 4 nights",
        "daily_budget": 110,
        "daily_mid": 240,
        "daily_luxury": 520
    }
    print(f"Location: {package['location']}, Price: ${package['budget']}, Duration: {package['duration']}")
    
    tier = input("Choose a daily travel style (Budget, Mid-range, Luxury): ").lower()
    if tier == "budget":
        print(f"Estimated daily cost: ${package['daily_budget']}/day")
    elif tier == "mid-range" or tier == "mid":
        print(f"Estimated daily cost: ${package['daily_mid']}/day")
    elif tier == "luxury":
        print(f"Estimated daily cost: ${package['daily_luxury']}/day")
    else:
        print("Invalid choice, showing standard rates.")

elif destination == "SANTORINI":
    print("We have the Santorini Guide for you!")
    package = {
        "location": "Santorini, Greece",
        "budget": 1650,
        "duration": "6 days / 5 nights",
        "daily_budget": 95,
        "daily_mid": 210,
        "daily_luxury": 480
    }
    print(f"Location: {package['location']}, Price: ${package['budget']}, Duration: {package['duration']}")
    
    tier = input("Choose a daily travel style (Budget, Mid-range, Luxury): ").lower()
    if tier == "budget":
        print(f"Estimated daily cost: ${package['daily_budget']}/day")
    elif tier == "mid-range" or tier == "mid":
        print(f"Estimated daily cost: ${package['daily_mid']}/day")
    elif tier == "luxury":
        print(f"Estimated daily cost: ${package['daily_luxury']}/day")
    else:
        print("Invalid choice, showing standard rates.")

else:
    print("Sorry, we don't have information for that destination.")

print("Wish you a great and wonderful trip!")
