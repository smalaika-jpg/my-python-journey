print("Hi Ayesha! ")
greetings = input("Enter your greeting's reply: ")
print("We are planning to throw a party for Laila")
pov = input("Enter your point of view regarding this (yes/no): ").lower()
if pov == "yes":
   print("We are really glad that you like it too.Lets find a good gift.")
   print("You should be with us as we are going to a shopping mall")
elif pov =="no":
    print("We are going to a shopping mall.We will join you in a short time!")
else:
    print("Errror! Invalid answer.")
def shopping_haul():
    items =  "suit,heels,crockery"
    return items

print(f"We are going to buy {shopping_haul()}for Laila.")

for i in range(3):
    print("We need to add something more to this...")

items_count = 4
if items_count > 3:
   print("Stop! I guess this is enough!")
   
try:
   with open("file.txt","w") as my_file:
       my_file.write("gift shopping\n")
       my_file.write("Today's experience\n")
   print("Success: Storage of daily life routine in my file.txt")

except:
   print("Error:File didnt save in file.txt")

print("That's all for today.") 