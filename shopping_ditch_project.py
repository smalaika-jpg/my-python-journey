# Shopping Ditch
print("Hi Eman!")

shopping_schedule = int(input("Enter the timings in which you wanna do shopping (in hours): "))

print(f"So the total time we have for shopping is {shopping_schedule} hours.")
brands_name = input("Enter the name of the brands from which you wanna do shopping: ")

if shopping_schedule <= 3:
    print("Congratulations! You are really good at time management.")
else:
    print("Dear! It seems like you find it really hard to choose one.")

print("Happy Shopping")